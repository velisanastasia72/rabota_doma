# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator
#
#
# @repeat(3)
# def say_hi():
#     print("Hi")
#
#
# say_hi()
# print("-" * 20)
#
#
#
#
#
# def multiply_by_two(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * 2
#     return wrapper
#
#
# @multiply_by_two
# def number(a, b):
#     return a + b
#
# print(number(a=2, b=3))
# print("-" * 20)




#
# is_admin = False
#
# def check_admin(func):
#     def wrapper(*args, **kwargs):
#         global is_admin
#         if not is_admin:
#             print("Доступ запрещен!")
#         else:
#             print("Hello World")
#     return wrapper
#
# @check_admin
# def some_action():
#     print("Выполняется секретное действие")
#
# print("Результат задания 3 (is_admin = False)")
# some_action()
#
# print("\nРезультат задания 3 (is_admin = True)")
# is_admin = True
# some_action()
#
# print("-" * 20)





def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print("Начало")
        result = func(*args, **kwargs)
        print("Конец")
        return result
    return wrapper

@start_end_decorator
def greet():
    print("Привет")


greet()


