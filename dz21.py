def test():

    filename = 'test_file_1.txt'

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Замена строки в текстовом файле;\n")
        f.write("изменить строку в списке;\n")
        f.write("записать список в файл;\n")

    pos1 = int(input("pos1 = "))
    pos2 = int(input("pos2 = "))

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if 1 <= pos1 <= len(lines) and 1 <= pos2 <= len(lines):
        lines[pos1 - 1], lines[pos2 - 1] = lines[pos2 - 1], lines[pos1 - 1]

        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(lines)

        print("\nРезультат в файле")
        print("".join(lines))
    else:
        print("Ошибка Номер строки выходит за пределы файла")


test()


def test_1():
    filename = 'test_file_2.txt'

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Замена строки в текстовом файле;\n")
        f.write("изменить строку в списке;\n")
        f.write("записать список в файл;\n")

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    reversed_lines = lines[::-1]

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(reversed_lines)

    print("Результат в файле:")
    print("".join(reversed_lines))


test_1()


def test_2():
    file1_name = 'first_file.txt'
    file2_name = 'second_file.txt'
    file3_name = 'third_file.txt'

    with open(file1_name, 'w', encoding='utf-8') as f:
        f.write("Это содержимое первого файла.\n")
        f.write("Строка 2 из первого файла.\n")

    with open(file2_name, 'w', encoding='utf-8') as f:
        f.write("Это содержимое второго файла.\n")
        f.write("Строка 2 из второго файла.\n")

    with open(file1_name, 'r', encoding='utf-8') as f1:
        content1 = f1.read()

    with open(file2_name, 'r', encoding='utf-8') as f2:
        content2 = f2.read()

    with open(file3_name, 'w', encoding='utf-8') as f3:
        f3.write(content1)
        if content1 and not content1.endswith('\n'):
            f3.write('\n')
        f3.write(content2)

    print(f"Файлы '{file1_name}' и '{file2_name}' успешно объединены в '{file3_name}'.")
    with open(file3_name, 'r', encoding='utf-8') as f3:
        print("\nСодержимое третьего файла:")
        print(f3.read())


test_2()