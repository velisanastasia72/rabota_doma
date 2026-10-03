import os
import datetime
import sys


def format_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} Б"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f} КБ"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.2f} МБ"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.2f} ГБ"


def main():
    if len(sys.argv) > 1:

        path = sys.argv[1]
    else:

        path = input("Введите путь к файлу или папке: ").strip()

    print("\n" + "=" * 40)
    print("       PATH INSPECTOR")
    print("=" * 40)

    if not os.path.exists(path):
        print("Указанный путь не существует.")
        return

    abs_path = os.path.abspath(path)
    print(f"Абсолютный путь: {abs_path}")

    if os.path.isfile(path):
        obj_type = "Файл"
        print(f" Тип объекта:    {obj_type}")

        size_bytes = os.path.getsize(path)
        size_readable = format_size(size_bytes)
        print(f" Размер:         {size_readable} ({size_bytes} байт)")

        mtime_timestamp = os.path.getmtime(path)
        mtime_readable = datetime.datetime.fromtimestamp(mtime_timestamp).strftime('%d.%m.%Y %H:%M:%S')
        print(f" Изменен:        {mtime_readable}")

    elif os.path.isdir(path):
        obj_type = "Директория"
        print(f" Тип объекта:    {obj_type}")

        try:
            items_count = len(os.listdir(path))
            print(f" Элементов внутри: {items_count}")

            mtime_timestamp = os.path.getmtime(path)
            mtime_readable = datetime.datetime.fromtimestamp(mtime_timestamp).strftime('%d.%m.%Y %H:%M:%S')
            print(f"🕒 Изменена:       {mtime_readable}")
        except PermissionError:
            print(" Нет прав доступа для чтения содержимого этой директории.")

    else:
        print("Тип объекта: Неизвестно")

    print("=" * 40)


if __name__ == "__main__":
    main()
