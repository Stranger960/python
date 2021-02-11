from random import randint as rn
from time import sleep as sl

class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell < other.cell:
            print(f"*** Wrong cells subtraction: {self.cell} - {other.cell}")
            return "hm... must be some confusion..."
        return self.cell - other.cell

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        return round(self.cell / other.cell, 0)

    def make_order(self, rows):
        print(f"\ncells = {self.cell}, rows = {rows}\nand nice printing:")
        n, rmd = self.cell // rows, self.cell % rows
        print(("*" * rows + "\n") * n + ("*" * rmd + "\n"))


c1, c2 = rn(15,25), rn(7,12)
print(f"\nCells random sizes:  {c1} & {c2}")
cell_1 = Cell(c1)
cell_2 = Cell(c2)
print(f"\nCells additions:    {cell_1 + cell_2}")
print(f"Cells subtraction:    {cell_1 - cell_2}")
print(f"Cells multiplication: {cell_1 * cell_2}")
print(f"Cells division:       {int(cell_1 / cell_2)}")
cell_1.make_order(5)

for k in range(10,0,-1):          #  спасибо за подсказку :-)
    print (f"\r{k}", end = "")
    sl(0.5)
print(f"\rDone !")