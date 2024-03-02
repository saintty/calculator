import unittest
from fractionalClass.RationalFraction import RationalFraction


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
        result = f1 ** f3 + f2 - f3 * f1 / f2
        self.assertEqual(str(result), "11/8")

    def test_power(self):
        self.assertEqual(str(RationalFraction("2") ** 3), "8/1")
        self.assertEqual(str(RationalFraction("2") ** (-3)), "1/8")
        self.assertEqual(str(RationalFraction("-2") ** 3), "-8/1")
        self.assertEqual(str(RationalFraction("-2") ** (-3)), "-1/8")
        self.assertEqual(str(RationalFraction("10") ** 0), "1/1")

        f = RationalFraction("2") ** 0.5
        self.assertAlmostEqual(f.numerator / f.denominator, 1.41421, places=4)
        f = RationalFraction("2") ** -0.5
        self.assertAlmostEqual(f.numerator / f.denominator, 0.7071, places=4)
        with self.assertRaises(ValueError):
            RationalFraction("-2") ** 0.5
        with self.assertRaises(ValueError):
            f = RationalFraction("-2") ** -0.5
        f = RationalFraction("2") ** 0.0
        self.assertAlmostEqual(f.numerator / f.denominator, 1, places=4)

        f = RationalFraction("2") ** RationalFraction("0.5")
        self.assertAlmostEqual(f.numerator / f.denominator, 1.41421, places=4)
        f = RationalFraction("2") ** RationalFraction("-0.5")
        self.assertAlmostEqual(f.numerator / f.denominator, 0.7071, places=4)
        with self.assertRaises(ValueError):
            RationalFraction("-2") ** RationalFraction("0.5")
        with self.assertRaises(ValueError):
            f = RationalFraction("-2") ** RationalFraction("-0.5")
        f = RationalFraction("2") ** RationalFraction("0.0")
        self.assertAlmostEqual(f.numerator / f.denominator, 1, places=4)


if __name__ == '__main__':
    unittest.main()
