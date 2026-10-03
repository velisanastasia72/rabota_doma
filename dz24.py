class Book:

    def __init__(self, title="", year=0, publisher="", genre="", author="", price=0.0):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price


    def input_data(self):
        print("\nВвод данных о книге")
        self.__title = input("Название книги:")

        while True:
            try:
                self.__year = int(input("Год выпуска:"))
                break
            except ValueError:
                print("Ошибка: год должен быть целым числом")

        self.__publisher = input("Издатель: ")
        self.__genre = input("Жанр: ")
        self.__author = input("Автор: ")

        while True:
            try:
                self.__price = float(input("Цена: "))
                break
            except ValueError:
                print("Ошибка: цена должна быть числом")

    def display_data(self):
        print("\nИнформация о книге")
        print(f"Название:  {self.__title}")
        print(f"Год:       {self.__year}")
        print(f"Издатель:  {self.__publisher}")
        print(f"Жанр:      {self.__genre}")
        print(f"Автор:     {self.__author}")
        print(f"Цена:      {self.__price:.2f}")


    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def get_publisher(self):
        return self.__publisher

    def get_genre(self):
        return self.__genre

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price


    def set_title(self, title):
        self.__title = title

    def set_year(self, year):
        if isinstance(year, int) and year > 0:
            self.__year = year
        else:
            print("Ошибка год должен быть положительным целым числом")

    def set_publisher(self, publisher):
        self.__publisher = publisher

    def set_genre(self, genre):
        self.__genre = genre

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        if isinstance(price, (int, float)) and price >= 0:
            self.__price = float(price)
        else:
            print("Ошибка цена должна быть неотрицательным числом.")


    def __str__(self):

        return (f"«{self.__title}» — {self.__author}, "
                f"{self.__year} г., {self.__publisher}, "
                f"{self.__genre}, {self.__price:.2f} руб.")



if __name__ == "__main__":
    print("Создание через конструктор")
    book1 = Book("капитанская дочь", 1933, "посредник", "пьеса", "александр пушкин", 500.0)
    book1.display_data()

    print(f"\nДоступ через геттер Автор: {book1.get_author()}")
    print(f"Доступ через геттер Цена: {book1.get_price():.2f}")

    book1.set_price(520.0)
    print(f"\nПосле изменения цены через геттер  Новая цена: {book1.get_price():.2f}")

    book1.set_year(-100)

    print(f"\nВывод через print(book): {book1}")

    print("\n" + "-" * 50)
    print("Ввод данных с клавиатуры")
    print("-" * 50)
    book2 = Book()
    book2.input_data()
    book2.display_data()