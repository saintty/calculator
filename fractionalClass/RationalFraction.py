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
        if isinstance(other, int) or isinstance(other, float):
            new_other = RationalFraction(str(other))
            return new_other
        elif isinstance(other, RationalFraction):
            return other
        else:
            raise ValueError("Operand must be a int, float or RationalFraction object")

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
        other = RationalFraction._check_instance(other)
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return RationalFraction._create_result(new_numerator, new_denominator)

    __radd__ = __add__

    def __sub__(self, other):
        other = RationalFraction._check_instance(other)
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return RationalFraction._create_result(new_numerator, new_denominator)

    def __rsub__(self, other):
        other = RationalFraction._check_instance(other)
        return other - self

    def __mul__(self, other):
        other = RationalFraction._check_instance(other)
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return RationalFraction._create_result(new_numerator, new_denominator)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = RationalFraction._check_instance(other)
        if other.numerator == 0:
            raise ZeroDivisionError("Division by 0")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return RationalFraction._create_result(new_numerator, new_denominator)

    def __rtruediv__(self, other):
        other = RationalFraction._check_instance(other)
        return other / self

    def __pow__(self, power):
        if isinstance(power, int):
            return self._pow_integer(power)
        elif isinstance(power, float):
            return self._pow_float(power)
        elif isinstance(power, RationalFraction):
            return self._pow_fraction(power)
        else:
            raise TypeError("Unsupported type")

    def _pow_integer(self, power):
        if power < 0:
            self.numerator, self.denominator = self.denominator, self.numerator
            if self.denominator < 0:
                self.denominator = abs(self.denominator)
                self.numerator = -self.numerator
            power = abs(power)
        new_numerator = self.numerator ** power
        new_denominator = self.denominator ** power
        return RationalFraction._create_result(new_numerator, new_denominator)

    def _pow_float(self, power):
        fractional_part = power - int(power)
        if fractional_part != 0 and self.numerator < 0:
            raise ValueError("Negative fraction to a non-integer power")
        result = (float(self.numerator) / float(self.denominator)) ** power
        return RationalFraction(str(result))

    def _pow_fraction(self, power):
        new_power = power.numerator / power.denominator
        if isinstance(new_power, int):
            return self._pow_integer(new_power)
        elif isinstance(new_power, float):
            return self._pow_float(new_power)
