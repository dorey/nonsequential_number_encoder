from nonsequentials import *

def print_demo(num):
    enc = nonsequential_encode(num)
    dec = nonsequential_decode(enc)
    print "[%s] encodes to [%s] which decodes to [%s]" % \
        (str(num), enc, dec)

print_demo(100)
print_demo(101)
print_demo(102)
