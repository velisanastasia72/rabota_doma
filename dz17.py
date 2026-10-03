# def enter():
#     s = input("Введите строку: ")
#
#     first_h = s.find('h')
#     last_h = s.rfind('h')
#
#     result = s[:first_h] + s[last_h + 1:]
#
#     print(result)
#
# # "I am learning Python. hello, WORLD!"
# enter()


# def test_1():
#     s = input("Введите строку: ")
#
#     first_h = s.find('h')
#     last_h = s.rfind('h')
#
#
#     part1 = s[:first_h + 1]
#
#     part2 = s[first_h + 1: last_h][::-1]
#
#
#     part3 = s[last_h:]
#
#     result = part1 + part2 + part3
#     print(result)
#  #
#  # "I am learning Python. hello, WORLD!"
#
# test_1()



#
# def test_2():
#     s = input("Строка: ")
#     old_sub = input("Ее заменяемая подстрока: ")
#     new_sub = input("Новая подстрока: ")
#
#     result = s.replace(old_sub, new_sub)
#
#     print(result)
#
# # Строка: 11 23 44 55 23 22
# # Заменяемая: 23
# # Новая: !!!
#
# test_2()

#
# def test_3():
#     print("Введите текст:")
#
#     text = ""
#     while True:
#         line = input()
#         if line == "":
#             break
#         text += line + " "
#
#     text_lower = text.lower()
#
#     words = text_lower.split()
#
#     count = 0
#     for word in words:
#         if word.startswith('е') or word.startswith('ё'):
#             count += 1
#
#     print(f"\nКоличество слов: {count}")
#
# # Текст ежевику для ежать
# # принесли два ежа
# # ежевику ели ели
# # ежата возле ели съели
# test_3()

