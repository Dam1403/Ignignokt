import struct
import os
#from Ignignokt.Executable.PEConstants import IMAGE_TYPEMAP# fix path issue
class PortableExecutable:


    def __init__(self, pathtofile):
        self.filepath = pathtofile

        with open(pathtofile, 'rb') as file:
            self._parse_dos(file)
            self._parse_coff(file)
            self._parse_std_optional_header(file)

            magic_pe32 = 0x10b
            magic_pe64 = 0x20b
            if self.magic_num in [magic_pe32, magic_pe64]:
                self._parse_win_optional_header(file)
                self._parse_win_data_directories(file)
                self._parse_section_table(file)
            i = 0

    def print_details(self):
        print(self.filepath)
    def _parse_dos(self,file_obj):
        # DOS HEADER
        DOSHeaderFormat = "<QQQQQQQII"
        # Nothing in this header matters but the pe_signatureOffset.
        self.PEheader_offset = struct.unpack(DOSHeaderFormat, file_obj.read(64))[-1]
    def _parse_coff(self, file_obj):
        # PE HEADER
        COFFHeaderFormat = "<IHHIIIHH"
        file_obj.seek(self.PEheader_offset)
        coff_chunks = struct.unpack(COFFHeaderFormat, file_obj.read(24))

        self.pe_signature = coff_chunks[0]
        self.machine_type = coff_chunks[1]
        self.number_of_sections = coff_chunks[2]
        self.timedate_stamp = coff_chunks[3]
        self.dep_symboltable = coff_chunks[4]
        self.dep_symbol_count = coff_chunks[5]
        self.optional_header_size = coff_chunks[6]
        self.characteristics = self._parse_characteristic_flags(coff_chunks[7])

    def _parse_characteristic_flags(self, val):
        curr_flag = 1
        flags = []
        while curr_flag <= 0x8000:
            if val & 1 == 1:
                flags.append(curr_flag)
            curr_flag <<= 1
        return flags

    def _parse_std_optional_header(self,file_obj):
        file_obj.seek(self.PEheader_offset + 24) # skip Coff header
        OPTHeaderFormat = "<HBBIIIIII"
        std_opt_chunks = struct.unpack(OPTHeaderFormat, file_obj.read(28))

        self.magic_num = std_opt_chunks[0]
        self.major_linker_vers = std_opt_chunks[1]
        self.minor_linker_vers = std_opt_chunks[2]
        self.size_of_code = std_opt_chunks[3]
        self.size_of_init_data = std_opt_chunks[4]
        self.size_of_uninit_data = std_opt_chunks[5]
        self.offset_entry_point = std_opt_chunks[6]

        magic_pe32 = 0x10b
        magic_pe64 = 0x20b
        if self.magic_num == magic_pe32:
            self.base_of_code = std_opt_chunks[7]

    def _parse_win_optional_header(self, file_obj):

        WINOPTHeaderFormat =   "<IIIHHHHHHIIIIHHIIIIII"
        WIN64OPTHeaderFormat = "<QIIHHHHHHIIIIHHQQQQII"

        magic_pe32 = 0x10b
        magic_pe64 = 0x20b
        if self.magic_num == magic_pe32:
            format = WINOPTHeaderFormat
            std_optsize = 28
        elif self.magic_num == magic_pe64:
            format = WIN64OPTHeaderFormat
            std_optsize = 24
        else:
            raise Exception("Attempted to  parse windows optional header on a non windows executable")
        file_obj.seek(self.PEheader_offset + 24 + std_optsize)
        print(self.optional_header_size - std_optsize)
        chunks = struct.unpack(format, file_obj.read(struct.calcsize(format)))

        self.image_base = chunks[0]
        self.section_alignment = chunks[1]
        self.file_alignment = chunks[2]
        self.major_os_version = chunks[3]
        self.minor_os_version = chunks[4]
        self.major_image_version = chunks[5]
        self.minor_image_version = chunks[6]
        self.major_subsystem_version = chunks[7]
        self.minor_subsystem_version = chunks[8]
        self.win32versionvalue = chunks[9] # Should be zero
        self.size_of_image = chunks[10]
        self.size_of_headers = chunks[11]
        self.check_sum = chunks[12]
        self.sub_system = chunks[13]
        self.dll_characteristics = chunks[14]
        self.size_of_stack_reserve = chunks[15]
        self.size_of_stack_commit = chunks[16]
        self.size_of_heap_reserve = chunks[17]
        self.size_of_heap_commit = chunks[18]
        self.loader_flags = chunks[19] # Should be zero
        self.number_of_rva_and_sizes = chunks[20]

        self.data_dir_offset = self.PEheader_offset + 24 + std_optsize + struct.calcsize(format)

    def _parse_win_data_directories(self, file_obj):
        magic_pe32 = 0x10b
        magic_pe64 = 0x20b

        file_obj.seek(self.data_dir_offset)

        data_dir_types = [
            "Export Table",
            "Import Table",
            "Resource Table",
            "Exception Table",
            "Certificate Table",
            "Base Relocation Table",
            "Debug",
            "Architecture",
            "Global Ptr",
            "TLS Table",
            "Load Config Table",
            "Bound Import",
            "IAT",
            "Delay Import Descriptor",
            "CLR Runtime Header",
            "Reserved, must be zero"
        ]
        self.data_directories = {}
        data_dir_entry_format = "<II"

        for i in range(0, self.number_of_rva_and_sizes):
            raw_dir_entry = file_obj.read(struct.calcsize(data_dir_entry_format))
            dir_entry = struct.unpack(data_dir_entry_format, raw_dir_entry)
            self.data_directories[data_dir_types[i]] = {"RVA": dir_entry[0], "Size": dir_entry[1]}

        self.section_table_offset = file_obj.tell()
        print(self.data_directories)

    def _parse_section_table(self, file_obj):
        file_obj.seek(self.section_table_offset)
        self.section_table = dict()
        section_header_fmt = "<IIIIIIHHI"
        for i in range(0, self.number_of_sections):
            name = file_obj.read(8).decode('ascii').replace("\0","")
            raw_section_header = file_obj.read(struct.calcsize(section_header_fmt))
            section_header_chunks = struct.unpack(section_header_fmt, raw_section_header)
            section_header = SectionHeader()
            section_header.Name = name
            section_header.VirtualSize = section_header_chunks[0]
            section_header.VirtualAddress = section_header_chunks[1]
            section_header.SizeOfRawData = section_header_chunks[2]
            section_header.PointerToRawData = section_header_chunks[3]
            section_header.PointerToRelocations = section_header_chunks[4]
            section_header.PointerToLineNumbers = section_header_chunks[5]
            section_header.NumberOfRelocations = section_header_chunks[6]
            section_header.NumberOfLineNumbers = section_header_chunks[7]
            section_header.Characteristics = section_header_chunks[8]
            self.section_table[name] = section_header
        print(self.section_table)

    def __str__(self):

        filename = os.path.split(self.filepath)[1]
        return f"Windows Portable Executable {filename}"


class SectionHeader:
    def __init__(self):
        self.Name = ""
        self.VirtualSize = 0
        self.VirtualAddress = 0
        self.SizeOfRawData = 0
        self.PointerToRawData = 0
        self.PointerToRelocations = 0
        self.PointerToLineNumbers = 0
        self.NumberOfRelocations = 0
        self.NumberOfLineNumbers = 0
        self.Characteristics = 0

    def __str__(self):
        return f"{self.Name} section at {hex(self.VirtualAddress)}"

