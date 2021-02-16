class Complex_data_operations:
    def __init__(self, cnum):
        self.zr = cnum.real
        self.zi = cnum.imag

    def __add__(self, other):
        return complex(self.zr + other.zr, self.zi + other.zi)

    def __mul__(self, other):
        a1, b1 = self.zr, self.zi
        a2, b2 = other.zr, other.zi
        return complex(a1 * a2 - b1 * b2, a1 * b2 + a2 * b1)


c1 = 1 + 11j
c2 = 2 + 22j
C_1 = Complex_data_operations(c1)
C_2 = Complex_data_operations(c2)

print(f"\nInitial data:\nc1 = {c1}\nc2 = {c2}\n")
print(f"c1 + c2 = {C_1 + C_2}")
print(f"c1 * c2 = {C_1 * C_2}")

s = c1 * c2
print(f"\nChecking with built-in function:\nc1 * c2 = {s}\n")