import math

class Rational:
    def __init__(self, numerator, denominator=None):
        if denominator is None:
            if isinstance(numerator, str):
                n, d = map(int, numerator.strip().split('/'))
            else:
                n, d = numerator, 1
        else:
            n, d = numerator, denominator

        if d == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        gcd = math.gcd(n, d)
        self.n = n // gcd
        self.d = d // gcd

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __add__(self, other):
        if isinstance(other, Rational):
            n = self.n * other.d + other.n * self.d
            d = self.d * other.d
        elif isinstance(other, int):
            n = self.n + other * self.d
            d = self.d
        else:
            raise TypeError("Unsupported type for addition.")
        return Rational(n, d)

    def __sub__(self, other):
        if isinstance(other, Rational):
            n = self.n * other.d - other.n * self.d
            d = self.d * other.d
        elif isinstance(other, int):
            n = self.n - other * self.d
            d = self.d
        else:
            raise TypeError("Unsupported type for subtraction.")
        return Rational(n, d)

    def __mul__(self, other):
        if isinstance(other, Rational):
            n = self.n * other.n
            d = self.d * other.d
        elif isinstance(other, int):
            n = self.n * other
            d = self.d
        else:
            raise TypeError("Unsupported type for multiplication.")
        return Rational(n, d)

    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.n == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            n = self.n * other.d
            d = self.d * other.n
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            n = self.n
            d = self.d * other
        else:
            raise TypeError("Unsupported type for division.")
        return Rational(n, d)

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == 'n':
            return self.n
        elif key == 'd':
            return self.d
        else:
            raise KeyError("Key must be 'n' for numerator or 'd' for denominator.")

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise ValueError("Only integer values are allowed.")
        if key == 'n':
            self.n = value
        elif key == 'd':
            if value == 0:
                raise ZeroDivisionError("Denominator cannot be zero.")
            self.d = value
        else:
            raise KeyError("Key must be 'n' for numerator or 'd' for denominator.")
        gcd = math.gcd(self.n, self.d)
        self.n //= gcd
        self.d //= gcd
