from abc import ABC, abstractmethod
import math


class Shape(ABC):


    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    def display_info(self):
        print(f"Цвет: {self.color}")
        print(f"Площадь: {round(self.area(), 2)}")
        print(f"Периметр: {round(self.perimeter(), 2)}")
        self.draw()
        print()


class Square(Shape):

    def __init__(self, side, color):
        super().__init__(color)
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4

    def draw(self):
        for _ in range(self.side):
            print("*" * self.side)

    def display_info(self):
        print("===Квадрат===")
        print(f"Сторона: {self.side}")
        super().display_info()


class Rectangle(Shape):


    def __init__(self, length, width, color):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def draw(self):
        for _ in range(self.width):
            print("*" * self.length)

    def display_info(self):
        print("===Прямоугольник===")
        print(f"Длина: {self.length}")
        print(f"Ширина: {self.width}")
        super().display_info()


class Triangle(Shape):

    def __init__(self, side1, side2, side3, color):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def draw(self):
        height = self.side1
        for i in range(1, height + 1):
            spaces = " " * (height - i)
            stars = "*" * (2 * i - 1)
            print(spaces + stars)

    def display_info(self):
        print("===Треугольник===")
        print(f"Сторона 1: {self.side1}")
        print(f"Сторона 2: {self.side2}")
        print(f"Сторона 3: {self.side3}")
        super().display_info()


if __name__ == '__main__':
    square = Square(3, "red")
    rectangle = Rectangle(7, 3, "green")  # Длина 7, Ширина 3 (чтобы площадь была 21)
    triangle = Triangle(6, 6, 11, "yellow")  # Стороны 6, 6, 11 (периметр 23)


    square.display_info()
    rectangle.display_info()
    triangle.display_info()