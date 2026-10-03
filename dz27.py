import tkinter as tk


class Line:

    def __init__(self, canvas, x1, y1, x2, y2, color='black', width=1):
        self.canvas = canvas
        for name, val in [('x1', x1), ('y1', y1), ('x2', x2), ('y2', y2)]:
            if not isinstance(val, int):
                raise TypeError(
                    f"Координата {name}={val} должна быть целочисленной! "
                    f"Получен тип {type(val).__name__}"
                )
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.color = color
        self.width = width
        self.draw()

    def draw(self):
        self.canvas.create_line(
            self.x1, self.y1, self.x2, self.y2,
            fill=self.color, width=self.width
        )


class Rect:


    def __init__(self, canvas, x1, y1, x2, y2, color='black', width=1):
        self.canvas = canvas

        for name, val in [('x1', x1), ('y1', y1), ('x2', x2), ('y2', y2)]:
            if not isinstance(val, (int, float)):
                raise TypeError(
                    f"Координата {name}={val} должна быть числом (int/float)! "
                    f"Получен тип {type(val).__name__}"
                )
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.color = color
        self.width = width
        self.draw()

    def draw(self):
        self.canvas.create_rectangle(
            self.x1, self.y1, self.x2, self.y2,
            outline=self.color, width=self.width
        )


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Домашнее задание — Line & Rect")
    canvas = tk.Canvas(root, width=600, height=400, bg='white')
    canvas.pack(padx=10, pady=10)

    try:
        print("Рисование линии: (1, 2), (10, 20), red, 1")
        line1 = Line(canvas, 1, 2, 10, 20, 'red', 1)


        print("\nРисование линии: (10.2, 20), (100, 200), green, 3")
        line2 = Line(canvas, 10.2, 20, 100, 200, 'green', 3)

    except TypeError as e:
        print(f"⚠️  Ошибка: {e}")

    try:

        print("\nРисование прямоугольника: (7, 9), (12, 15), red, 1")
        rect1 = Rect(canvas, 7, 9, 12, 15, 'red', 1)


        print("Рисование прямоугольника: (30.5, 40.2), (50, 60), red, 1")
        rect2 = Rect(canvas, 30.5, 40.2, 50, 60, 'red', 1)

    except TypeError as e:
        print(f"️  Ошибка: {e}")

    root.mainloop()