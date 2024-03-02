from math import gcd
from math import pow

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


    def d__pow__(self, other):
        #if isinstance(other, RationalFraction):
        #power = RationalFraction(str(other))
        if other < 0:
            self.numerator, self.denominator = self.denominator, self.numerator
            other = abs(other)

        new_numerator = self.numerator ** other
        decimal_part = int(new_numerator)
        fractional_part = new_numerator - decimal_part
        t = 10 ** len(str(fractional_part))

        new_denominator = self.denominator ** other
        decimal_part = int(new_numerator)
        fractional_part = new_numerator - decimal_part
        k = 10 ** len(str(fractional_part))
        t = max(t, k)
        new_numerator *= t
        new_denominator *= t
        print(new_numerator)
        print(new_denominator)
        return RationalFraction._create_result(new_numerator, new_denominator)

    def __pow__(self, power):
        if isinstance(power, int):
            if power < 0:
                self.numerator, self.denominator = self.denominator, self.numerator
                if self.denominator < 0:
                    self.denominator = abs(self.denominator)
                    self.numerator = -self.numerator
                power = abs(power)
            new_numerator = self.numerator ** power
            new_denominator = self.denominator ** power
            return RationalFraction._create_result(new_numerator, new_denominator)
        elif isinstance(power, float):
            result = pow(float(self.numerator) / float(self.denominator), power)
            return RationalFraction(str(result))
        elif isinstance(power, RationalFraction):
            result = pow(float(self.numerator) / float(self.denominator), float(power.numerator) / float(power.denominator))
            return RationalFraction(str(result))



