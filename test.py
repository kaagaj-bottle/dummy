import unittest
from fractions import Fraction

from my_sum import sum


class TestSum(unittest.TestCase):

    def test_list_int(self):

        data = [1, 2, 3, 4]
        result = sum(data)
        self.assertEqual(result, 10)

    def test_list_fraction(self):

        data = [Fraction(1, 2), Fraction(1, 4), Fraction(1, 4)]
        result = sum(data)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
