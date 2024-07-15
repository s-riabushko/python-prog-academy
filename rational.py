import math


class Rational:
    """
    Class Rational for compare, addition, multiplication and subtraction of simple fractions
    """
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int):
            raise TypeError(f"Numerator must be integers, got {type(numerator).__name__}.")
        if not isinstance(denominator, int):
            raise TypeError(f"Denominator must be integers, got {type(denominator).__name__}.")
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        elif isinstance(other, tuple) and len(other) == 2:
            other = Rational(other[0], other[1])
        elif not isinstance(other, Rational):
            return NotImplemented
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        elif isinstance(other, tuple) and len(other) == 2:
            other = Rational(other[0], other[1])
        elif not isinstance(other, Rational):
            return NotImplemented
        return self.numerator * other.denominator != other.numerator * self.denominator

    def __lt__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        elif isinstance(other, tuple) and len(other) == 2:
            other = Rational(other[0], other[1])
        elif not isinstance(other, Rational):
            return NotImplemented
        if self.numerator / self.denominator < 0 <= other.numerator / other.denominator:
            return False
        if other.numerator / other.denominator < 0 <= self.numerator / self.denominator:
            return True
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        elif isinstance(other, tuple) and len(other) == 2:
            other = Rational(other[0], other[1])
        elif not isinstance(other, Rational):
            return NotImplemented
        if self.numerator / self.denominator < 0 <= other.numerator / other.denominator:
            return False
        if other.numerator / other.denominator < 0 <= self.numerator / self.denominator:
            return True
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        elif isinstance(other, tuple) and len(other) == 2:
            other = Rational(other[0], other[1])
        elif not isinstance(other, Rational):
            return NotImplemented
        if self.numerator / self.denominator >= 0 > other.numerator / other.denominator:
            return True
        if other.numerator / other.denominator >= 0 > self.numerator / self.denominator:
            return False
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        elif isinstance(other, tuple) and len(other) == 2:
            other = Rational(other[0], other[1])
        elif not isinstance(other, Rational):
            return NotImplemented
        if self.numerator / self.denominator >= 0 > other.numerator / other.denominator:
            return True
        if other.numerator / other.denominator >= 0 > self.numerator / self.denominator:
            return False
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        elif isinstance(other, tuple) and len(other) == 2:
            other = Rational(other[0], other[1])
        elif not isinstance(other, Rational):
            return NotImplemented
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        tmp = self + other
        self.numerator = tmp.numerator
        self.denominator = tmp.denominator
        return self

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        elif isinstance(other, tuple) and len(other) == 2:
            other = Rational(other[0], other[1])
        elif not isinstance(other, Rational):
            return NotImplemented
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        tmp = self - other
        self.numerator = tmp.numerator
        self.denominator = tmp.denominator
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        elif isinstance(other, tuple) and len(other) == 2:
            other = Rational(other[0], other[1])
        elif not isinstance(other, Rational):
            return NotImplemented
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        tmp = self * other
        self.numerator = tmp.numerator
        self.denominator = tmp.denominator
        return self

    def __str__(self):
        if self.numerator == 0:
            return '0'
        if self.numerator == self.denominator:
            return '1'
        gcd = math.gcd(self.numerator, self.denominator)
        tmp_numerator = abs(self.numerator // gcd)
        tmp_denominator = abs(self.denominator // gcd)
        if tmp_denominator == 1:
            return f'{tmp_numerator}'
        sign = '-' if self.numerator * self.denominator < 0 else ''
        if tmp_numerator > tmp_denominator:
            whole = tmp_numerator // tmp_denominator
            tmp_numerator = tmp_numerator % tmp_denominator
            return f'{sign}{whole} {tmp_numerator}/{tmp_denominator}'

        return f'{sign}{tmp_numerator}/{tmp_denominator}'


if __name__ == '__main__':
    # HW 05 Task 3
    print("\nTask 3")
    x = Rational(3, 11)
    y = Rational(7, -8)
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"x > y: {x > y}")
    print(f"x + y: {x + y}")
    print(f"x - y: {x - y}")
    print(f"y - x: {y - x}")
    print(f"x * y: {x * y}")
