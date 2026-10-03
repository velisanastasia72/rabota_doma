import json
import os


FILE_NAME = "countries.json"


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Файл сохранен")



def add_country(countries, **kwargs):
    country = kwargs.get('country')
    capital = kwargs.get('capital')

    if country in countries:
        print(f"Страна '{country}' уже существует! Используйте редактирование.")
    else:
        countries[country] = capital
        save_data(countries)


def delete_country(countries, *args):
    if not args:
        print("Ошибка: не передано название страны.")
        return

    country = args[0]
    if country in countries:
        del countries[country]
        save_data(countries)
        print(f"Страна '{country}' удалена.")
    else:
        print(f"Страна '{country}' не найдена.")


def search_country(countries, *args):
    if not args: return
    country = args[0]
    capital = countries.get(country)

    if capital:
        print(f"Столица страны '{country}': {capital}")
    else:
        print(f"Информация о стране '{country}' не найдена.")


def edit_country(countries, **kwargs):
    country = kwargs.get('country')
    new_capital = kwargs.get('capital')

    if country in countries:
        countries[country] = new_capital
        save_data(countries)
        print(f"Столица страны '{country}' изменена на '{new_capital}'.")
    else:
        print(f"Страна '{country}' не найдена.")


def view_all(countries):
    if not countries:
        print("Список стран пуст.")
    else:
        print(countries)




if __name__ == '__main__':
    countries_db = load_data()

    while True:
        print("\n***************")
        print("Выбор действия:")
        print("1 - добавление данных")
        print("2 - удаление данных")
        print("3 - поиск данных")
        print("4 - редактирование данных")
        print("5 - просмотр данных")
        print("6 - завершение работы")

        choice = input("Ввод: ")

        if choice == '1':
            c_name = input("Введите название страны (с заглавной буквы): ")
            c_cap = input("Введите название столицы страны (с заглавной буквы): ")
            add_country(countries_db, country=c_name, capital=c_cap)

        elif choice == '2':
            c_name = input("Введите название страны для удаления: ")
            delete_country(countries_db, c_name)

        elif choice == '3':
            c_name = input("Введите название страны для поиска: ")
            search_country(countries_db, c_name)

        elif choice == '4':
            c_name = input("Введите название страны для редактирования: ")
            new_cap = input("Введите новое название столицы: ")
            edit_country(countries_db, country=c_name, capital=new_cap)

        elif choice == '5':
            view_all(countries_db)

        elif choice == '6':
            print("Работа завершена.")
            break

        else:
            print("Неверный выбор, попробуйте снова.")