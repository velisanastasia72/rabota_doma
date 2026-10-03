# def slovar():
#
#     dict1 = {1: 10, 2: 20}
#     dict2 = {3: 30, 4: 40}
#     dict3 = {5: 50, 6: 60}
#
#     result_dict = dict1.copy()
#     result_dict.update(dict2)
#     result_dict.update(dict3)
#
#
#     print(result_dict)
#
# slovar()

#
# def staff():
#
#     employees = {
#         'emp1': {'name': 'Jhon', 'salary': 7500},
#         'emp2': {'name': 'Emma', 'salary': 8000},
#         'emp3': {'name': 'Brad', 'salary': 6500}
#     }
#
#     print(employees['emp3'])
#     print(employees['emp3']['salary'])
#
#
#     employees['emp3']['salary'] = 8500
#
#     print("emp1")
#     print(f"name : {employees['emp1']['name']}")
#     print(f"salary : {employees['emp1']['salary']}")
#
#     print("emp2")
#     print(f"name : {employees['emp2']['name']}")
#     print(f"salary : {employees['emp2']['salary']}")
#
#     print("emp3")
#     print(f"name : {employees['emp3']['name']}")
#     print(f"salary : {employees['emp3']['salary']}")
#
#
#
# staff()


def student_2():


    try:
        n = int(input("Количество студентов"))

        students_data = []
        total_score = 0

        for i in range(1, n + 1):
            name = input(f"{i}-й студент:")
            score = int(input("Балл: "))

            students_data.append({"name": name, "score": score})
            total_score += score

        if n > 0:
            average_score = round(total_score / n)
        else:
            average_score = 0

        print(f"\nСредний балл: {average_score}. Студенты с баллом выше среднего")

        for student in students_data:
            if student["score"] > average_score:
                print(student["name"])

    except ValueError:
        print("Ошибка ввода")

student_2()