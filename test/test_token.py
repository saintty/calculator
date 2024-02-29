import unittest

from utils.token import Token


class TestPrime(unittest.TestCase):
    def test_type(self):
        self.assertEqual(Token(Token.number, 0).type, Token.number)
        self.assertEqual(Token(Token.variable, 0).type, Token.variable)
        self.assertEqual(Token(Token.operation, 0).type, Token.operation)

    def test_value(self):
        self.assertEqual(Token(Token.variable, "var_name").value, "var_name")
        self.assertEqual(Token(Token.number, 1).value, 1)
        self.assertEqual(Token(Token.number, 1.9481094809).value, 1.9481094809)
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
