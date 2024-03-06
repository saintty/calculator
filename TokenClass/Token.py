class Token:
    variable = "Variable"
    number = "Operand"
    operation = "Operation"
    unary_operation = "Unary Operand"

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return "({}: {})".format(self.type, self.value)

    def __add__(self, other_token):
        return Token(Token.number, self.value + other_token.value)

    def __sub__(self, other_token):
        return Token(Token.number, self.value - other_token.value)

    def __pow__(self, other_token):
        return Token(Token.number, self.value ** other_token.value)

    def __mul__(self, other_token):
        return Token(Token.number, self.value * other_token.value)

    def __truediv__(self, other_token):
        return Token(Token.number, self.value / other_token.value)


__all__ = ["Token"]
