import random


def task_1():
    rows = 4
    cols = 3
    matrix = []


    for i in range(rows):
        row = []
        for j in range(cols):
            num = random.randint(-20, 10)
            row.append(num)
        matrix.append(row)


        print(f"{row[0]}\t{row[1]}\t{row[2]}\t")


    negative_count = 0
    for row in matrix:
        for num in row:
            if num < 0:
                negative_count += 1

    print(f"Количество отрицательных элементов: {negative_count}")
    print("-" * 20)


task_1()


def task_2():
    rows = 4
    cols = 3
    matrix = []


    for i in range(rows):
        row = []
        for j in range(cols):
            num = random.randint(0, 4)
            row.append(num)
        matrix.append(row)
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t")


    product = 1
    has_non_zero = False

    for row in matrix:
        for num in row:
            if num != 0:
                product *= num
                has_non_zero = True


    if not has_non_zero:
        product = 0

    print(f"Произведение ненулевых элементов: {product}")
    print("-" * 20)


task_2()


def task_3():
    size = 6
    matrix = []


    for i in range(size):
        row = []
        for j in range(size):
            num = random.randint(0, 10)
            row.append(num)
        matrix.append(row)

    single_list = [random.randint(0, 10) for _ in range(size)]

    print("Исходная матрица:")
    for row in matrix:
        print("\t".join(map(str, row)))

    print(f"Одномерный список: {single_list}")

    for i in range(0, size, 2):
        matrix[i] = single_list[:]


    print("\nРезультат после замены:")
    for row in matrix:
        print("\t".join(map(str, row)))


task_3()