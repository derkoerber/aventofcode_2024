import unittest

from main import check_row, process


input = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]


class TestDay1(unittest.TestCase):

    def test_check_row(self):
        self.assertEqual(True, check_row(input[0]))
        self.assertEqual(False, check_row(input[1]))
        self.assertEqual(False, check_row(input[2]))
        self.assertEqual(False, check_row(input[3]))
        self.assertEqual(False, check_row(input[4]))
        self.assertEqual(True, check_row(input[5]))

    def test_process(self):
        self.assertEqual(2, process(input))

if __name__ == '__main__':
    unittest.main()