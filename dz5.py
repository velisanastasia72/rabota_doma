# def task_1():
#     print(" Выведите все элементы списка с четными индексами")
#     print("Введите элементы списка")
#
#     try:
#         n = int(input("n = "))
#         my_list = []
#
#         for i in range(n):
#             val = int(input(f"-> "))
#             my_list.append(val)
#
#         result = my_list[::2]
#
#         print(*result)
#
#     except ValueError:
#         print("Ошибка введите целые числа")
#
#
#
# task_1()
#
#
# def task_2():
#     print("\n Выведите все элементы списка которые больше предыдущего элемента")
#     print("Введите элементы списка")
#
#     try:
#         n = int(input("n = "))
#         my_list = []
#
#         for i in range(n):
#             val = int(input(f"-> "))
#             my_list.append(val)
#
#         result = []
#         for i in range(1, len(my_list)):
#             if my_list[i] > my_list[i - 1]:
#                 result.append(my_list[i])
#
#         print(*result)
#
#     except ValueError:
#         print("Ошибка: Введите целые числа.")
#
#
#
# task_2()

#
# def task_3():
#     print("\n Вывести треугольник из звездочек")
#
#     height = 8
#
#     print("")
#     for i in range(1, height + 1):
#         print("*" * i)
#
#     print("")
#     for i in range(height, 0, -1):
#         print("*" * i)
#
#
#
# task_3()