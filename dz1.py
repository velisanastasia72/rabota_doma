
number = input("Введите пятизначное число: ")


if len(number) == 5 and number.isdigit():
    digits = [int(d) for d in number]

    product = 1
    for d in digits:
        product *= d


    average = sum(digits) / len(digits)

    print(f"Произведение цифр числа {number}: {product}")
    print(f"Среднее арифметическое: {average}")
else:
    print("Ошибка: нужно ввести пятизначное число!")


print("\nВведите четыре числа:")
a = float(input("1: "))
b = float(input("2: "))
c = float(input("3: "))
d = float(input("4: "))

sum_first = a + b
sum_second = c + d


if sum_second != 0:
    result = sum_first / sum_second
    print(f"Результат: {result:.2f}")
else:
    print("Ошибка: деление на ноль!")



a = 1
b = 2

print(f"До обмена: а = {a}, b = {b}")

a, b = b, a

print(f"После обмена: a = {a}, b = {b}")
