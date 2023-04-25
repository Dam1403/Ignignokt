IMAGE_TYPEMAP ={
    0: 'Unknown',
    332: 'Intel 386 or later processors and compatible processors',
    358: 'MIPS little endian',
    361: '',
    388: 'Alpha AXP, 32-bit address space',
    418: 'Hitachi SH3',
    419: 'Hitachi SH3 DSP',
    422: 'Hitachi SH4',
    424: 'Hitachi SH5',
    448: 'ARM little endian',
    450: 'Thumb',
    452: 'ARM Thumb-2 little endian',
    467: 'Matsushita AM33',
    496: 'Power PC little endian',
    497: 'Power PC with floating point support',
    512: 'Intel Itanium processor family',
    614: 'MIPS16',
    644: 'AXP 64 (Same as Alpha 64)',
    870: 'MIPS with FPU',
    1126: 'MIPS16 with FPU',
    3772: 'EFI byte code',
    20530: 'RISC-V 32-bit address space',
    20580: 'RISC-V 64-bit address space',
    20776: 'RISC-V 128-bit address space',
    25138: 'LoongArch 32-bit processor family',
    25188: 'LoongArch 64-bit processor family',
    34404: 'x64',
    36929: 'Mitsubishi M32R little endian',
    43620: 'ARM64 little endian'
}

CHARACTERISTICS_MAP = {
    1: {   'long_name': 'Image only, Windows CE, and Microsoft Windows NT and '
                        'later. This indicates that the file does not contain '
                        'base relocations and must therefore be loaded at its '
                        'preferred base address. If the base address is not '
                        'available, the loader reports an error. The default '
                        'behavior of the linker is to strip base relocations '
                        'from executable (EXE) files.',
           'short_name': 'IMAGE_FILE_RELOCS_STRIPPED'},
    2: {   'long_name': 'Image only. This indicates that the image file is '
                        'valid and can be run. If this flag is not set, it '
                        'indicates a linker error.',
           'short_name': 'IMAGE_FILE_EXECUTABLE_IMAGE'},
    4: {   'long_name': 'COFF line numbers have been removed. This flag is '
                        'deprecated and should be zero.',
           'short_name': 'IMAGE_FILE_LINE_NUMS_STRIPPED'},
    8: {   'long_name': 'COFF symbol table entries for local symbols have been '
                        'removed. This flag is deprecated and should be zero.',
           'short_name': 'IMAGE_FILE_LOCAL_SYMS_STRIPPED'},
    16: {   'long_name': 'Obsolete. Aggressively trim working set. This flag '
                         'is deprecated for Windows 2000 and later and must be '
                         'zero.',
            'short_name': 'IMAGE_FILE_AGGRESSIVE_WS_TRIM'},
    32: {   'long_name': 'Application can handle > 2-GB addresses.',
            'short_name': 'IMAGE_FILE_LARGE_ADDRESS_ AWARE'},
    64: {   'long_name': 'This flag is reserved for future use.',
            'short_name': 'IMAGE_FILE_LARGE_ADDRESS_ AWARE'},
    128: {   'long_name': 'Little endian: the least significant bit (LSB) '
                          'precedes the most significant bit (MSB) in memory. '
                          'This flag is deprecated and should be zero.',
             'short_name': 'IMAGE_FILE_BYTES_REVERSED_LO'},
    256: {   'long_name': 'Machine is based on a 32-bit-word architecture.',
             'short_name': 'IMAGE_FILE_32BIT_MACHINE'},
    512: {   'long_name': 'Debugging information is removed from the image '
                          'file.',
             'short_name': 'IMAGE_FILE_DEBUG_STRIPPED'},
    1024: {   'long_name': 'If the image is on removable media, fully load it '
                           'and copy it to the swap file.',
              'short_name': 'IMAGE_FILE_REMOVABLE_RUN_ FROM_SWAP'},
    2048: {   'long_name': 'If the image is on network media, fully load it '
                           'and copy it to the swap file.',
              'short_name': 'IMAGE_FILE_NET_RUN_FROM_SWAP'},
    4096: {   'long_name': 'The image file is a system file, not a user '
                           'program.',
              'short_name': 'IMAGE_FILE_SYSTEM'},
    8192: {   'long_name': 'The image file is a dynamic-link library (DLL). '
                           'Such files are considered executable files for '
                           'almost all purposes, although they cannot be '
                           'directly run.',
              'short_name': 'IMAGE_FILE_DLL'},
    16384: {   'long_name': 'The file should be run only on a uniprocessor '
                            'machine.',
               'short_name': 'IMAGE_FILE_UP_SYSTEM_ONLY'},
    32768: {   'long_name': 'Big endian: the MSB precedes the LSB in memory. '
                            'This flag is deprecated and should be zero.',
               'short_name': 'IMAGE_FILE_BYTES_REVERSED_HI'}
}
