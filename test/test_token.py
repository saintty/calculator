import unittest

from fractionalClass.RationalFraction import RationalFraction
from TokenClass.Token import Token


class TestPrime(unittest.TestCase):
    def test_type(self):
        self.assertEqual(
            Token(Token.number, RationalFraction("0")).type, Token.number)
        self.assertEqual(
            Token(Token.variable, RationalFraction("0")).type, Token.variable)
        self.assertEqual(
            Token(Token.operation, RationalFraction("0")).type, Token.operation)

    def test_value(self):
        self.assertEqual(Token(Token.variable, "var_name").value, "var_name")
        self.assertEqual(
            str(Token(Token.number, RationalFraction("1")).value), "1/1")
        self.assertEqual(str(Token(Token.number, RationalFraction(
            "1.9481094809")).value), "19481094809/10000000000")
        self.assertEqual(
            str(Token(Token.number, RationalFraction("-2")).value), "-2/1")
        self.assertEqual(
            str(Token(Token.number, RationalFraction("-2.5")).value), "-5/2")
        self.assertEqual(Token(Token.operation, "+").value, "+")
        self.assertEqual(Token(Token.operation, "-").value, "-")
        self.assertEqual(Token(Token.operation, "*").value, "*")
        self.assertEqual(Token(Token.operation, "/").value, "/")
        self.assertEqual(Token(Token.operation, "^").value, "^")

    def test_add(self):
        result_token = Token(Token.number, 1) + Token(Token.number, 2)
        self.assertEqual(result_token.value, 3)

    def test_sub(self):
        result_token = Token(Token.number, 1) - Token(Token.number, 2)
        self.assertEqual(result_token.value, -1)

    def test_mul(self):
        result_token = Token(Token.number, 1) * Token(Token.number, 2)
        self.assertEqual(result_token.value, 2)

    def test_div(self):
        result_token = Token(Token.number, 1) / Token(Token.number, 2)
        self.assertEqual(result_token.value, 0.5)

    def test_pow(self):
        result_token = Token(Token.number, 1) ** Token(Token.number, 2)
        self.assertEqual(result_token.value, 1)


if __name__ == '__main__':
    unittest.main()
