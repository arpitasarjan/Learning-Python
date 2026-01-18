class Complex:
    def __init__(self, r, i):
        self.r = r  # real part
        self.i = i  # imaginary part

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        real = self.r * other.r - self.i * other.i
        imag = self.r * other.i + self.i * other.r
        return Complex(real, imag)

    def __str__(self):
        return f"{self.r} + {self.i}i"

# Test the implementation
c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)  # Output: 4 + 6i
print(c1 * c2)  # Output: -5 + 10i