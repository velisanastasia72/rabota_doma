def convert_temperature(value, scale):
    scale = scale.upper()

    if scale == 'C':
        result = value * 1.8 + 32
        print(f"{value} C -> {result} F")

    elif scale == 'F':
        result = (value - 32) / 1.8
        result_rounded = round(result, 2)
        print(f"{value} F -> {result_rounded} C")

    else:
        print("Ошибка: Неизвестная шкала ")


print("")
convert_temperature(23, 'C')
convert_temperature(63, 'F')
print("-" * 20)


def change(lst):
    if len(lst) < 2:
        return lst

    lst[0], lst[-1] = lst[-1], lst[0]

    return lst


print("проверка")

data1 = [1, 2, 3]
data2 = [9, 12, 33, 54, 105]
data3 = ['к', 'л', 'а', 'н']

print("Исходные данные")
print(data1)
print(data2)
print(data3)

change(data1)
change(data2)
change(data3)

print("Результат:")
print(data1)
print(data2)
print(data3)
