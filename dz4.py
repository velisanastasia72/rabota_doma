def guess_the_number_game():

    secret_number = 66

    attempts = 0
    print("Добро пожаловать в игру Угадай число")
    print("Я загадал число от 1 до 100. Попробуй угадать")
    print("Если захотите выйти введите 0.")


    while True:
        try:
            user_input = input("\nВведите число от 1 до 100: ")
            guess = int(user_input)


            if guess == 0:
                print("Вы вышли из игры загаданное число было:", secret_number)
                break


            attempts += 1


            if guess < 1 or guess > 100:
                print("вводите числа только в диапазоне от 1 до 100.")

                attempts -= 1
                continue

            if guess < secret_number:
                print("Загаданное число больше")
            elif guess > secret_number:
                print("Загаданное число меньше")
            else:

                print(f"Вы угадали загаданное число с {attempts} раза")
                break

        except ValueError:
            print("Ошибка: введите целое число56")



if __name__ == "__main__":
    guess_the_number_game()