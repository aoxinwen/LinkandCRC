# coding = "utf-8"

import crcmod.predefined
import sys


class CRCGenerator(object):
    def __init__(self):
        self.module = 'crc-8-maxim'

    def create(self, input):
        crc8 = crcmod.predefined.Crc(self.module)
        # hexData = binascii.unhexlify(input)
        hexData = bytes.fromhex(input)
        crc8.update(hexData)
        if crc8.crcValue < 16:
            result = "0" + format(crc8.crcValue, 'x')
        else:
            result = format(crc8.crcValue, 'x')
        return result


def CRCGenerator2():
    crc_module = crcmod.predefined.Crc(sys.argv[1])
    hexData = bytes.fromhex(sys.argv[2])
    crc_module.update(hexData)
    if crc_module.crcValue < 16:
        result = "0" + format(crc_module.crcValue, 'x')
    else:
        result = format(crc_module.crcValue, 'x')
    return result


if __name__ == "__main__":
    CRCGenerator2()
