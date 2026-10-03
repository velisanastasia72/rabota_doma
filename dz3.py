def calculator():
    print("Добро пожаловать в программу «Калькулятор»!")

    while True:
        print("\n" + "=" * 40)
        print("Выберите операцию:")
        print('1 - "r" - применяет унарный минус к операнду')
        print('2 - "+" - сложение')
        print('3 - "-" - вычитание')
        print('4 - "/" - деление')
        print('5 - "*" - умножение')
        print('6 - "%" - деление  (остаток от деления)')
        print('7 - "<" - минимальное из двух чисел')
        print('8 - ">" - максимальное из двух чисел')
        print('0 - "STOP" - остановить работу')
        print("=" * 40)

        operation = input("Введите номер операции: ")

        if operation == '0':
            print("Работа калькулятора остановлена. До свидания!")
            break

        if operation not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Ошибка: Неверный номер операции. Пожалуйста, попробуйте снова.")
            continue

        try:

            if operation == '1':
                num1 = float(input("Введите число: "))
                result = -num1
                print(f"Результат: -({num1}) = {result}")


            else:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                result = 0

                if operation == '2':
                    result = num1 + num2
                    print(f"Результат: {num1} + {num2} = {result}")

                elif operation == '3':
                    result = num1 - num2
                    print(f"Результат: {num1} - {num2} = {result}")

                elif operation == '4':
                    if num2 == 0:
                        print("Делить на ноль нельзя")
                    else:
                        result = num1 / num2
                        print(f"Результат: {num1} / {num2} = {result}")

                elif operation == '5':
                    result = num1 * num2
                    print(f"Результат: {num1} * {num2} = {result}")

                elif operation == '6':
                    if num2 == 0:
                        print("Делить на ноль нельзя")
                    else:
                        result = num1 % num2
                        print(f"Результат: {num1} % {num2} = {result}")

                elif operation == '7':
                    result = min(num1, num2)
                    print(f"Минимальное число: {result}")

                elif operation == '8':
                    result = max(num1, num2)
                    print(f"Максимальное число: {result}")

        except ValueError:
            print("Ошибка: Введено некорректное число. Пожалуйста, используйте цифры и точку/запятую.")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    calculator()
