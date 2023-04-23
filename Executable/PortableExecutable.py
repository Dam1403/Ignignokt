

import struct



DOSHeaderFormat = "<QQQQQQQII"
class PortableExecutable:


    def __init__(self, pathtofile):
        with open(pathtofile,'rb') as file:

            #DOS HEADER
            #Nothing in this header matters but the PESignatureOffset.
            self.PEheader_offset = struct.unpack(DOSHeaderFormat, file.read(64))[-1]
            file.seek(self.PEheader_offset)

            #PE HEADER
            self.PESignature = file.read(4)

    def __str__(self):
        return f"Windows Executable:\n PEHeader at {hex(self.PEheader_offset)} is {self.PESignature}"


