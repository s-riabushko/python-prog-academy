import math


class Rational:
    def __init__(self, a: int, b: int):
        if not isinstance(a | b, int):
            raise TypeError('numerator and denominator must be an integer')
        if b <= 0:
            raise ValueError('denominator must be greater then zero')
        self.__gcd = math.gcd(a, b)
        self.a = a // self.__gcd
        self.b = b // self.__gcd

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __ne__(self, other):
        return self.a != other.a or self.b != other.b

    def __lt__(self, other):
        return self.a * other.b < other.a * self.b

    def __le__(self, other):
        return self.a * other.b <= other.a * self.b

    def __gt__(self, other):
        return self.a * other.b > other.a * self.b

    def __ge__(self, other):
        return self.a * other.b >= other.a * self.b

    def __add__(self, other):
        num = self.a * other.b + other.a * self.b
        denom = self.b * other.b
        return Rational(num, denom)

    def __sub__(self, other):
        num = self.a * other.b - other.a * self.b
        denom = self.b * other.b
        return Rational(num, denom)

    def __mul__(self, other):
        num = self.a * other.a
        denom = self.b * other.b
        return Rational(num, denom)

    def __str__(self):
        if self.a == 0:
            return '0'
        if self.a == self.b:
            return '1'
        int_part = abs(self.a) // self.b
        if int_part:
            a = abs(self.a) % self.b
            return f"{'-' if self.a < 0 else ''}{int_part} {a}/{self.b}"
        else:
            return f"{self.a}/{self.b}"
