import math


def calculate_area():
    print("Калькулятор площади фигур")

    while True:
        print("\nВыберите фигуру:")
        print("1 - прямоугольник")
        print("2 - треугольник")
        print("3 - круг")
        print("0 - выход")

        choice = input("Введите номер фигуры (1-3)")

        if choice == '0':
            print("Программа завершена")
            break


        if choice not in ['1', '2', '3']:
            print("Неверный выбор введите 1, 2, 3 или 0.")
            continue

        try:

            if choice == '1':
                a = float(input("Введите длину первой стороны: "))
                b = float(input("Введите длину второй стороны: "))

                if a <= 0 or b <= 0:
                    print("Ошибка: Длины сторон должны быть больше нуля")
                else:
                    area = a * b
                    print(f"Площадь прямоугольника: {area:.2f}")

            elif choice == '2':
                base = float(input("Основание: "))
                height = float(input("Высота: "))

                if base <= 0 or height <= 0:
                    print("Ошибка: Основание и высота должны быть больше нуля")
                else:
                    area = 0.5 * base * height
                    print(f"Площадь: {area:.2f}")

            elif choice == '3':
                r = float(input("Введите радиус круга "))

                if r <= 0:
                    print("Ошибка радиус должен быть больше нуля")
                else:
                    area = math.pi * (r ** 2)
                    print(f"Площадь круга: {area:.2f}")

        except ValueError:
            print("Ошибка ввода попробуйте снова")


if __name__ == "__main__":
    calculate_area()