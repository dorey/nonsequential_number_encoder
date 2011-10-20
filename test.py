from nonsequentials import *
import unittest

def encode_decode(num):
    return nonsequential_decode(nonsequential_encode(num))

class TestSequenceFunctions(unittest.TestCase):
    def test_encode_decode(self):
        self.assertEqual(123, encode_decode(123))

if __name__ == '__main__':
    unittest.main()