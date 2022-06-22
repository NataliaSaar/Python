# 1. Python class for semaphore lights
import time
class TrafficLight:
    __color = ['green', 'yellow', 'red']
    def running(self):
        idx = 0
    #    while idx in len(self.__color.count()):
        for idx in range(3):
            color = TrafficLight.__color.__getitem__(idx)
            if idx == 1:
                timer = 2
            else:
                timer = 7
            print(color)
            time.sleep(timer)
            idx += 1

execute_sem = TrafficLight()
execute_sem.running()

# 2. Python class Road

class Road:
    __length: int
    __width: int
    __weight: int
    __thickness: int
    def __init__(self, length, width, weight = 25, thickness = 5):
        self.__length = length
        self.__width = width
        self.__weight = weight
        self.__thickness = thickness
    def count(self):
        result = self.__length * self.__width * self.__weight * self.__thickness / 1000
        print(f'{self.__length}m * {self.__width}m * {self.__weight}kg * {self.__thickness}sm = {result}t')

m5 = Road(1000,100)
m5.count()

# 3. Class for Workers

class Worker:
    name: str
    surname: str
    position: str
    _income = {}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income.__setitem__('wage', wage)
        self._income.__setitem__('bonus', bonus)


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
    #    print(self._income.items())
        result = sum(map(float, self._income.values()))
        print(f'Workers salary is {result}')

Worker1 = Position(name='Vasya', surname='Pupkin', position='engineer', wage=1000, bonus=500)
Worker1.get_full_name()
Worker1.get_total_income()

# 4. Python Car class
class Car:
    speed: int
    color: str
    name: str
    is_police: bool
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.is_police = is_police
        self.speed = speed
    def go(self):
        print(f'Car {self.color} {self.name} is going now.')
    def stop(self):
        print(f'Car {self.color} {self.name} has stopped.')
    def turn(self, direction):
        print(f'Car {self.color} {self.name} has turned to the {direction}.')
    def show_speed(self):
        print(f'Car {self.color} {self.name} has speed {self.speed}.')

class TownCar(Car):
    def show_speed(self):
        print(f'Car {self.color} {self.name} has speed {self.speed}!')
        if self.speed > 60:
            print(f'Thats overspeeding!')
        else:
            print('Thats fine.')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print(f'Car {self.color} {self.name} has speed {self.speed}!')
        if self.speed > 40:
            print(f'Thats overspeeding!')
        else:
            print('Thats fine.')

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
         super(PoliceCar, self).__init__(name, color, speed)
         self.is_police = is_police
Car1 = WorkCar(name='CAT', color='orange', speed=100)
Car2 = PoliceCar(name='Chevrolet Camaro', color='black', speed=200)
Car3 = SportCar(name='Mazda', color='red', speed=300)
Car4 = TownCar(name='FIAT', color='grey', speed=60)

Car1.go()
Car1.show_speed()
Car2.turn('left')
Car2.show_speed()
Car3.stop()
Car3.show_speed()
Car4.turn('right')
Car4.show_speed()

# 6. Python classes for Stationary

class Stationery:
    title = str
    def draw(self):
        print('Start drawing')
class Pen(Stationery):
    title = 'Pen'
    def draw(self):
        print(f'Start drawing with {self.title}')

class Pencil(Stationery):
    title = 'Pencil'
    def draw(self):
        print(f'Start drawing with {self.title}')

class Handle(Stationery):
    title = 'Handle'
    def draw(self):
        print(f'Start drawing with {self.title}')

Stationery1 = Stationery()
Stationery1.draw()

Stationery2 = Pen()
Stationery2.draw()

Stationery3 = Pencil()
Stationery3.draw()

Stationery4 = Handle()
Stationery4.draw()
