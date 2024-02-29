import unittest
from RationalFraction import RationalFraction


class TestRationalFraction(unittest.TestCase):
    def test_init(self):
        fraction = RationalFraction("3.14")
        self.assertEqual(fraction.numerator, 157)
        self.assertEqual(fraction.denominator, 50)

        fraction = RationalFraction("0")
        self.assertEqual(fraction.numerator, 0)
        self.assertEqual(fraction.denominator, 1)

        fraction = RationalFraction("8")
        self.assertEqual(fraction.numerator, 8)
        self.assertEqual(fraction.denominator, 1)

    def test_add(self):
        fraction1 = RationalFraction("3.14")
        fraction2 = RationalFraction("2.71")
        result = fraction1 + fraction2
        self.assertEqual(str(result), "117/20")

    def test_subtract(self):
        fraction1 = RationalFraction("5.99")
        fraction2 = RationalFraction("10.24")
        result = fraction1 - fraction2
        self.assertEqual(str(result), "-17/4")

    def test_multiply(self):
        fraction1 = RationalFraction("12.4567")
        fraction2 = RationalFraction("22")
        result = fraction1 * fraction2
        self.assertEqual(str(result), "1370237/5000")

    def test_divide(self):
        fraction1 = RationalFraction("20.5128")
        fraction2 = RationalFraction("3.6")
        result = fraction1 / fraction2
        self.assertEqual(str(result), "2849/500")

    def test_divide_by_zero(self):
        fraction1 = RationalFraction("3.14")
        fraction2 = RationalFraction("0")
        with self.assertRaises(ZeroDivisionError):
            fraction1 / fraction2

    def test_simple_expression(self):
        f1 = RationalFraction("0.5")
        f2 = RationalFraction("2")
        f3 = RationalFraction("3")
        result = f1 + f2 - f3 * f1 / f2
        self.assertEqual(str(result), "7/4")


if __name__ == '__main__':
    unittest.main()
