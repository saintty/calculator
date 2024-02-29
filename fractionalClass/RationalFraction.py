from math import gcd


class RationalFraction:
    __slots__ = ('numerator', 'denominator')

    def __init__(self, num_str):
        number = float(num_str)
        decimal_part = int(number)
        fractional_part = number - decimal_part
        if fractional_part == 0:
            self.numerator = decimal_part
            self.denominator = 1
        else:
            self.denominator = 10 ** len(str(fractional_part))
            self.numerator = int(self.denominator * number)
            self._simplify()

    def _simplify(self):
        divisor = gcd(self.numerator, self.denominator)
        self.numerator //= divisor
        self.denominator //= divisor

    @staticmethod
    def _check_instance(other):
        if not isinstance(other, RationalFraction):
            raise ValueError("Operand must be a RationalFraction object")

    @staticmethod
    def _create_result(numerator, denominator):
        result = RationalFraction("0")
        result.numerator = numerator
        result.denominator = denominator
        result._simplify()
        return result

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        RationalFraction._check_instance(other)
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return RationalFraction._create_result(new_numerator, new_denominator)

    def __sub__(self, other):
        RationalFraction._check_instance(other)
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return RationalFraction._create_result(new_numerator, new_denominator)

    def __mul__(self, other):
        RationalFraction._check_instance(other)
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return RationalFraction._create_result(new_numerator, new_denominator)

    def __truediv__(self, other):
        RationalFraction._check_instance(other)
        if other.numerator == 0:
            raise ZeroDivisionError("Division by 0")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return RationalFraction._create_result(new_numerator, new_denominator)


__all__ = ["RationalFraction"]
