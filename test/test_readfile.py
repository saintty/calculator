import unittest
import os

from utils.readfile import readFile, make_tokens, make_rpn, calculate
from utils.token import Token


class TestPrime(unittest.TestCase):
    def test_make_token(self):
        line = "1 + 2 + 3"
        expected = [
            Token(Token.number, 1),
            Token(Token.operation, "+"),
            Token(Token.number, 2),
            Token(Token.operation, "+"),
            Token(Token.number, 3)
        ]

        tokens = make_tokens(line)

        self.assertEqual(len(expected), len(tokens))
        for i in range(len(expected)):
            self.assertEqual(tokens[i].type, expected[i].type)
            self.assertEqual(tokens[i].value, expected[i].value)

    def test_make_rpn(self):
        line = "1 + 3 * (alpha - 8 / great)"
        tokens = make_tokens(line)
        expected = [
            Token(Token.number, 1),
            Token(Token.number, 3),
            Token(Token.variable, "alpha"),
            Token(Token.number, 8),
            Token(Token.variable, "great"),
            Token(Token.operation, "/"),
            Token(Token.operation, "-"),
            Token(Token.operation, "*"),
            Token(Token.operation, "+"),
        ]

        rpn = make_rpn(line)

        self.assertEqual(len(expected), len(rpn))
        for i in range(len(rpn)):
            self.assertEqual(rpn[i].type, expected[i].type)
            self.assertEqual(rpn[i].value, expected[i].value)


if __name__ == '__main__':
    unittest.main()
