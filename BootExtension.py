import sys


# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

def passcalc(seed):
    value = int(seed, 0 if seed.startswith("0x") else 16) # http://stackoverflow.com/questions/209513/convert-hex-string-to-int-in-python
    # a = first 3 bytes of seed value
    a = value >> 24
    b = a + 0x10F0A563
    # c = (last byte of seed value) AND 7
    c = value & 7
    # password = (b ROR c)  XOR a
    return ror(b, c, 32) ^ a


if len(sys.argv) > 1:
    seed = sys.argv[1]
    print(hex(passcalc(seed))[2:].upper())
elif __name__ == '__main__':
    tests = [("000CF448B61F", "AE21ED90"),
             ("000D4548B61F", "5021EC20"),
             ("00011748B61F", "F421E05B")]
    for t in tests:
        password = hex(passcalc(t[0]))[2:].upper()
        print(t[0], password, password == t[1])
