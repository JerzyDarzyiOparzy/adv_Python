from abc import ABC, abstractmethod
import math


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_circumference(self):
        pass

    def __lt__(self, other):
        if isinstance(other, Figure):
            return self.get_area() < other.get_area()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Figure):
            return self.get_area() > other.get_area()
        return NotImplemented


class Square(Figure):
    def __init__(self, side=1):
        self.side = side

    def __str__(self) -> str:
        return f"Square({self.side})"

    def __add__(self, other):
        if isinstance(other, Square):
            new_side = math.sqrt(self.side ** 2 + other.side ** 2)
            return Square(new_side)
        elif isinstance(other, int):
            return Square(self.side + other)
        else:
            raise TypeError("Unsupported operand for +: Square and {}".format(type(other).__name__))

    def __radd__(self, other):
        if isinstance(other, int):
            return Square(self.side + other)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Square):
            self.side = math.sqrt(self.side ** 2 + other.side ** 2)
        elif isinstance(other, int):
            self.side += other
        else:
            raise TypeError("Unsupported operand for +=: Square and {}".format(type(other).__name__))
        return self

    def __mul__(self, scale: int | float):
        return Square(self.side * scale)

    def __truediv__(self, scale: int | float):
        return Square(self.side / scale)

    def __eq__(self, other):
        return isinstance(other, Square) and self.side == other.side

    def get_area(self):
        return self.side ** 2

    def get_circumference(self):
        return 4 * self.side


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_circumference(self):
        return 2 * math.pi * self.radius


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Field({self.value})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return isinstance(other, Field) and self.value == other.value

    def __setattr__(self, name, value):
        if name == "value":
            if isinstance(value, int) and 10 <= value <= 2000:
                super().__setattr__(name, value)
            elif isinstance(value, str):
                super().__setattr__(name, value)
            else:
                raise TypeError("Invalid value type. Must be int (10-2000) or str.")
        else:
            super().__setattr__(name, value)


# Testy
if __name__ == '__main__':
    s1 = Square(3)
    s2 = Square(4)
    print(s1 + s2)  # Dodawanie dwóch kwadratów
    print(s1 + 2)  # Dodawanie liczby całkowitej
    print(2 + s1)  # Odwrotna kolejność dodawania
    s1 += s2
    print(s1)  # += dla dwóch kwadratów
    s1 += 2
    print(s1)  # += dla int

    print(s1.get_area())
    print(s1.get_circumference())

    c1 = Circle(5)
    print(c1.get_area())
    print(c1.get_circumference())

    print(s1 > c1)  # Porównanie pól
    print(s1 < c1)

    f1 = Field(100)
    f2 = Field("Bankrut")
    print(f1, f2)
    try:
        f3 = Field(5000)
    except TypeError as e:
        print(e)
    try:
        f4 = Field(5.5)
    except TypeError as e:
        print(e)
