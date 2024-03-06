import unittest

from VectorClass.Vector import Vector
from fractionalClass.RationalFraction import RationalFraction


class TestRationalFraction(unittest.TestCase):
    def test_init(self):
        vector = Vector([RationalFraction(str(0)), RationalFraction(str(1)), RationalFraction(str(2))])
        self.assertEqual(str(vector), "0/1 1/1 2/1")

        vector = Vector([RationalFraction(str(-2)), RationalFraction(str(1.1)), RationalFraction(str(2.5))])
        self.assertEqual(str(vector), "-2/1 11/10 5/2")

    def test_add(self):
        v1 = Vector([RationalFraction(str(0)), RationalFraction(str(1)), RationalFraction(str(2))])
        v2 = Vector([RationalFraction(str(3)), RationalFraction(str(4)), RationalFraction(str(5))])
        r1 = RationalFraction(str(5))
        result = v1 + v2
        self.assertEqual(str(result), "3/1 5/1 7/1")
        result = v2 + v1
        self.assertEqual(str(result), "3/1 5/1 7/1")
        result = r1 + v1
        self.assertEqual(str(result), "5/1 6/1 7/1")
        result = v1 + r1
        self.assertEqual(str(result), "5/1 6/1 7/1")

    def test_subtract(self):
        v1 = Vector([RationalFraction(str(0)), RationalFraction(str(1)), RationalFraction(str(2))])
        v2 = Vector([RationalFraction(str(3)), RationalFraction(str(4)), RationalFraction(str(5))])
        r1 = RationalFraction(str(5))
        result = v1 - v2
        self.assertEqual(str(result), "-3/1 -3/1 -3/1")
        result = v2 - v1
        self.assertEqual(str(result), "3/1 3/1 3/1")
        result = r1 - v1
        self.assertEqual(str(result), "Invalid operation")
        result = v1 - r1
        self.assertEqual(str(result), "-5/1 -4/1 -3/1")

    def test_multiply(self):
        v1 = Vector([RationalFraction(str(0)), RationalFraction(str(1)), RationalFraction(str(2))])
        v2 = Vector([RationalFraction(str(3)), RationalFraction(str(4)), RationalFraction(str(5))])
        r1 = RationalFraction(str(5))
        result = v1 * v2
        self.assertEqual(str(result), "14/1")
        result = v2 * v1
        self.assertEqual(str(result), "14/1")
        result = r1 * v1
        self.assertEqual(str(result), "0/1 5/1 10/1")
        result = v1 * r1
        self.assertEqual(str(result), "0/1 5/1 10/1")

    def test_divide(self):
        v1 = Vector([RationalFraction(2), RationalFraction(6), RationalFraction(10)])
        v2 = Vector([RationalFraction(1), RationalFraction(3), RationalFraction(5)])
        v3 = Vector([RationalFraction(str(0)), RationalFraction(str(1))])
        v4 = Vector([RationalFraction(str(3)), RationalFraction(str(4))])
        r1 = RationalFraction(str(5))
        result = v1 / v2
        self.assertEqual(str(result), "2/1")
        result = v2 / v1
        self.assertEqual(str(result), "1/2")
        result = v3 / v4
        self.assertEqual(str(result), "Invalid operation")
        result = v1 / r1
        self.assertEqual(str(result), "2/5 6/5 2/1")
        result = r1 / v1
        self.assertEqual(str(result), "Invalid operation")


if __name__ == '__main__':
    unittest.main()
