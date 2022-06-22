# 1. Python Matrix class
class Matrix:
    string1 = []
    string2 = []
    string3 = []
    def __init__(self, attrs: [[], [], []]):
        self._attributes = list(attrs)
    def __str__(self):
            self.string1 = self._attributes.__getitem__(0)
            self.string2 = self._attributes.__getitem__(1)
            self.string3 = self._attributes.__getitem__(2)
            return f'\n {self.string1} \n {self.string2} \n {self.string3}'
    def __add__(self, other):
        return Matrix([[self.string1.__getitem__(0) + other.string1.__getitem__(0),
                      self.string1.__getitem__(1) + other.string1.__getitem__(1),
                      self.string1.__getitem__(2) + other.string1.__getitem__(2)],
                      [self.string2.__getitem__(0) + other.string2.__getitem__(0),
                      self.string2.__getitem__(1) + other.string2.__getitem__(1),
                      self.string2.__getitem__(2) + other.string2.__getitem__(2)],
                      [self.string3.__getitem__(0) + other.string3.__getitem__(0),
                      self.string3.__getitem__(1) + other.string3.__getitem__(1),
                      self.string3.__getitem__(2) + other.string3.__getitem__(2)]])


listoflists1 = [1, 2, 3], [4, 5, 6], [7, 8, 9]
listoflists2 = [3, 2, 1], [6, 5, 4], [9, 8, 7]

Matrix1 = Matrix(listoflists1)
print(Matrix1.__str__())
Matrix2 = Matrix(listoflists2)
print(Matrix2.__str__())
print(Matrix1 + Matrix2)

# 2. Python class for tissue consumption calculating
class Clothes:
    def __init__(self, name, height=0, size=0):
        self.name = name
    @property
    def tc_calculate(self):
        if self.name == 'Coat':
            return self.size / 6.5 + 0.5
        elif self.name == 'Suit':
            return 2 * self.height + 0.3
        else:
            return 'n/a'

class Coat(Clothes):
    def __init__(self, size: int, name='Coat'):
        super(Coat, self).__init__(name)
        self.size = size
    def print_tc(self):
        print(f'Tissue consumption of this coat is {self.tc_calculate}.')

class Suit(Clothes):
    def __init__(self, height: int, name='Suit'):
        super(Suit, self).__init__(name)
        self.height = height
    def print_tc(self):
        print(f'Tissue consumption of this coat is {self.tc_calculate}.')

Coat1 = Coat(42)
Coat1.print_tc()
Suit1 = Suit(42)
Suit1.print_tc()

# 3. Python class for work with Cells

class Cell:
    def __init__(self, unit: int):
        self.unit = unit
    def __add__(self, other):
        return Cell(self.unit + other.unit)
    def __sub__(self, other):
        if self.unit - other.unit >= 0:
            return Cell(self.unit - other.unit)
        else:
            return 'Its impossible to execute subtraction!'
    def __mul__(self, other):
        return Cell(self.unit * other.unit)
    def __truediv__(self, other):
        return Cell(self.unit / other.unit)
    def make_order(self, col):
        self.col = col
        print_str = ''
        while self.unit >= self.col:
            row = '*' * self.col
            print_str = f'{print_str}\n{row}'
            self.unit = self.unit - self.col
        row = '*' * self.unit
        print_str = f'{print_str}\n{row}'
        print(print_str)

cell1 = Cell(17)
cell2 = Cell(5)
cell3 = cell1 / cell2
cell4 = cell1 * cell2
cell5 = cell1 - cell2
cell6 = cell2 - cell1
cell7 = cell1 + cell2
print(cell3.unit)
print(cell4.unit)
print(cell5.unit)
print(cell6)
print(cell7.unit)

cell1.make_order(5)
