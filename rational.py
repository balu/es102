class Rational:
    def __init__(self, p, q):
        self.numerator = p
        self.denominator = q
    
    def __mul__(self, other):
        return Rational(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

r0 = Rational(1, 2)
print(r0)
r1 = Rational(1, 3)
print(r1)
r2 = r0 * r1
print(r2)