def nonsequential_encode(num, digits=10, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    #Using base36 encode to have a character (or 2) at the end
    # of the xforms id_string that signifies the version number
    # this way, xforms exported on the same day do not have the
    # same ID string.
    if num == 0:
        return alphabet[0]
    num = int(str(num).rjust(digits, '0')[::-1])
    base36 = ''
    while num != 0:
        num, i = divmod(num, len(alphabet))
        base36 = alphabet[i] + base36
    return base36.upper()

def nonsequential_decode(estr):
    return int(str(int(estr, 36))[::-1])

print nonsequential_decode(nonsequential_encode(100))
print nonsequential_decode(nonsequential_encode(101))
print nonsequential_decode(nonsequential_encode(102))
