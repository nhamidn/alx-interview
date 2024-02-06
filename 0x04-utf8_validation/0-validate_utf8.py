#!/usr/bin/python3
"""
0-validate_utf8 Module.
"""


def validUTF8(data):
    """
    Method that determines if a given data set represents
    a valid UTF-8 encoding.
    """

    nb_bytes = 0
    for n in data:

        lsb = n & 0xFF
        if nb_bytes == 0:
            bit_count = 0
            for i in range(8):
                if (lsb & (1 << (7 - i)) != 0):
                    bit_count += 1
                else:
                    break

            if bit_count == 0:
                continue
            elif bit_count == 1 or bit_count > 4:
                return False
            nb_bytes = bit_count - 1
        else:
            if lsb & 128 == 0:
                return False
            else:
                if lsb & 64 != 0:
                    return False
            nb_bytes -= 1

    if nb_bytes != 0:
        return False
    return True
