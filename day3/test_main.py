import unittest

from main import calculate_mul, process


input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

class TestDay1(unittest.TestCase):

    def test_calculate_mul(self):
        self.assertEqual(8, calculate_mul("(2,4)%&mul[3,7]!@^do_not_mul"))
        self.assertEqual(88, calculate_mul("(11,8)mul(8,5))"))
        self.assertEqual(0, calculate_mul("asdasd(11,8)mul(8,5))"))
        self.assertEqual(0, calculate_mul("(1s1,d8)mul(8,5))"))
        

    def test_process(self):
        self.assertEqual(161, process(input, "p1"))
        self.assertEqual(161, process(input, "p2"))

if __name__ == '__main__':
    unittest.main()