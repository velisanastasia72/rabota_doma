# def corc_1():
#
#     my_tuple = ('ab', 'abcd', 'cde', 'abc', 'def')
#     print(f"Исходный кортеж: {my_tuple}")
#
#     s = input("s = ")
#
#     if s in my_tuple:
#         print("да")
#     else:
#         print("нет")
#
# corc_1()

#
# def corc_2():
#
#     user_input = input("Введите по порядку")
#
#     my_tuple = tuple(user_input)
#     print(my_tuple)
#
#     counted = []
#
#     for item in my_tuple:
#         if item not in counted:
#             count = my_tuple.count(item)
#             print(f"Количество {item} = {count}")
#             counted.append(item)
#
#
# corc_2()