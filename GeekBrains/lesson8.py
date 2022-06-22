# 1. Python Date class
class Date:
    date_str: str

    def __init__(self, date_str: str):
        self.date_str = date_str

    @classmethod
    def extraction(cls, date_str):
        cls.date_str = date_str
        values = cls.date_str.split('-')
        day = int(values.__getitem__(0))
        month = int(values.__getitem__(1))
        year = int(values.__getitem__(2))
        print(f'day: {day}, month: {month}, year: {year}')

    @staticmethod
    def validation(date_str):
        values = date_str.split('-')
        day = int(values.__getitem__(0))
        month = int(values.__getitem__(1))
        year = int(values.__getitem__(2))
        if day <= 31 and month in [1, 3, 5, 7, 8, 10, 12] or day <= 30 and month in [4, 6, 9, 11] or day <= 28 and month == 2:
            print(f'Date {date_str} is correct')
        else:
            print(f'Date {date_str} is incorrect! Please type correct date in day-month-year format.')


birthdate = Date('13-05-1988')
print(birthdate.date_str)
Date.extraction('13-05-1988')
Date.validation('13-05-1988')
Date.validation('13-25-1988')

# 2. Python ZeroDivision Exception
class ZeroDivider(Exception):
    print('Zero Division Exception')


def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ZeroDivider


try:
    division(10, 0)
except ZeroDivider:
    print('Oops! Its impossible to divide to zero!')

# 3. Python number list validator
class Validator(Exception):

    @classmethod
    def validation(cls, num_list: [int]):
        cls.num_list = num_list
        try:
            num_list = list(map(int, num_list))
            return num_list
        except ValueError:
            print('OopsIsNotANumberError')
            return 1


num_list = []
while True:
    input_str = input('Please type list of numbers with space separator, or "stop" if you want to finish:\n')
    if input_str == 'stop':
        print(f'Here is list of numbers you typed:\n{num_list}')
        print('bye!')
        break
    elif Validator.validation(input_str.split()) == 1:
        pass
    else:
        num_list.extend(Validator.validation(input_str.split()))

# 4. Python classes for office equipment
class OfficeEquipment:
    name: str
    price: int

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Printer(OfficeEquipment):

    def __init__(self, name, price, monochrome: bool, paint_type: str):
        super(Printer, self).__init__(name, price)
        self.monochrome = monochrome
        self.paint_type = paint_type


class Scanner(OfficeEquipment):

    def __init__(self, name, price, scan_type: str):
        super(Scanner, self).__init__(name, price)
        self.scan_type = scan_type


class Copier(OfficeEquipment):

    def __init__(self, name, price, monochrome: bool, paper_format: str):
        super(Copier, self).__init__(name, price)
        self.monochrome = monochrome
        self.paper_format = paper_format


class OfficeStorage(OfficeEquipment):

    capacity: int
    amount: int
    contents: dict

    def __init__(self, store_name, capacity, amount=0, contents=dict()):
        self.store_name = store_name
        self.capacity = capacity
        self.amount = amount
        self.contents = contents

    def storing(self, name, amount):
        self.amount = amount
        if StorageErrors.NoIntError(self.amount) == 0:
            if self.capacity >= self.amount + amount:
                self.contents.__setitem__(name, amount)
                self.amount = self.amount + amount
            else:
                print(self.contents)
                print(f'Not enough space. Only {self.capacity - self.amount} places left, you trying to put {amount}')
        elif StorageErrors.NoIntError(amount) == 1:
            pass
        else:
            print('n/a')

    def assignment(self, name, amount, location):
        self.amount = amount
        if StorageErrors.NoIntError(self.amount) == 0:
            if name in self.contents.keys():
                actual_amount = self.contents.get(name)
                if actual_amount >= amount:
                    self.contents.update({name: (actual_amount - amount)})
                    print(f'Assignment request successfully completed. {amount} item/s of {name} transfered to {location}\nFollowing items left in storage: {self.contents}')
                else:
                    print(f'Assignment request cant be completes, not enough items stored.\nFollowing items are stored now: {self.contents}')
            else:
                print(f'Requested item does not exist in storage\nFollowing items are stored now: {self.contents}')
        elif StorageErrors.NoIntError(amount) == 1:
            pass
        else:
            print('n/a')


class StorageErrors(Exception):
    @classmethod
    def NoIntError(cls, amount):
        cls.amount = amount
        try:
            if type(cls.amount) == int:
                return 0
            elif type(cls.amount) != int:
                print('Oops! Amount value should be integer, skipping.')
                return 1
        except TypeError:
            return 1


Storage1 = OfficeStorage('Storage1', 10)
Printer1 = Printer('Printer1', 100, True, 'Ink')
Printer2 = Printer('Printer2', 200, False, 'Laser')
Scanner1 = Scanner('Scanner1', 100, 'Flatbed')
Scanner2 = Scanner('Scanner2', 150, 'Drum')
Copier1 = Copier('Copier1', 100, True, 'A4')
Copier2 = Printer('Copier2', 170, True, 'A3')

Storage1.storing('Printer1', 'two')
Storage1.storing('Printer2', 2)
Storage1.storing('Scanner1', 2)
Storage1.storing('Scanner2', 2)
Storage1.storing('Copier1', 2)
Storage1.storing('Copier2', 2)

Storage1.assignment('Copier1', 1, 'IT-departnemt')
Storage1.assignment('Copier1', 3, 'IT-departnemt')
Storage1.assignment('Copier1', 'Tree', 'IT-departnemt')

# 7. Python class for Operations with Complex Numbers

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return ComplexNumber((self.real * other.real - self.imag * other.imag),
                             (self.real * other.imag + other.real * self.imag))

    def __str__(self):
        return f'{self.real}{"+" if self.imag > 0 else ""}{self.imag}i'


num1 = ComplexNumber(2, -9)
num2 = ComplexNumber(-5, 7)
print(num1 + num2)
print(num1 * num2)
