class PositiveNumber:


    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 0)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Атрибут '{self.name}' должен быть числом.")

        if value <= 0:
            raise ValueError(f"Атрибут '{self.name}' должен быть положительным числом. Получено: {value}")


        instance.__dict__[self.name] = value


class Order:


    price = PositiveNumber('price')
    quantity = PositiveNumber('quantity')

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

    def __str__(self):
        return f"Заказ: {self.name}, Цена: {self.price}, Кол-во: {self.quantity}"


if __name__ == '__main__':
    try:
        order = Order('apple', 5, 10)


        print(order.total_cost())



    except (ValueError, TypeError) as e:
        print(f"Ошибка ввода: {e}")