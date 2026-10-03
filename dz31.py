class Point3D:


    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        if other.x == 0 or other.y == 0 or other.z == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return Point3D(self.x / other.x, self.y / other.y, self.z / other.z)


    def __eq__(self, other):
        return (self.x == other.x and
                self.y == other.y and
                self.z == other.z)

    def __ne__(self, other):
        return not self.__eq__(other)


    def __getitem__(self, key):
        if key == "x": return self.x
        elif key == "y": return self.y
        elif key == "z": return self.z
        else: raise KeyError(f"Недопустимый ключ: {key}. Используйте 'x', 'y' или 'z'.")

    def __setitem__(self, key, value):
        if key == "x": self.x = value
        elif key == "y": self.y = value
        elif key == "z": self.z = value
        else: raise KeyError(f"Недопустимый ключ: {key}. Используйте 'x', 'y' или 'z'.")

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"


if __name__ == '__main__':
    p1 = Point3D(12, 15, 18)
    p2 = Point3D(6, 3, 9)

    print(f"Координаты 1-й точки: {p1.x}, {p1.y}, {p1.z}")
    print(f"Координаты 2-й точки: {p2.x}, {p2.y}, {p2.z}")


    print(f"\nСложение координат: {p1 + p2}")
    print(f"Вычитание координат: {p1 - p2}")
    print(f"Умножение: {p1 * p2}")
    print(f"Деление: {p1 / p2}")

    # Сравнение
    print(f"\nРавенство координат: {p1 == p2}")


    print(f"\nx = {p1['x']} x1 = {p2['x']}")
    print(f"y = {p1['y']} y1 = {p2['y']}")
    print(f"z = {p1['z']} z1 = {p2['z']}")


    p1["x"] = 20
    print(f"\nЗапись значения в координату x: {p1['x']}")