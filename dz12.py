# def people():
#
#     data = [("Иван", 25), ("Мария", 23), ("Петр", 25), ("Анна", 23)]
#     result_dict = {}
#
#     for name, age in data:
#         if age in result_dict:
#             result_dict[age].append(name)
#         else:
#             result_dict[age] = [name]
#
#     print(result_dict)
#
#
# people()

#
# def massive_one():
#
#     nums = [1, 1, 1, 2, 2, 3]
#     k = 3
#
#     counts = {}
#     for num in nums:
#         counts[num] = counts.get(num, 0) + 1
#
#     sorted_elements = sorted(counts.items(), key=lambda x: x[1], reverse=True)
#
#
#     result_k = 2
#     most_common = [item[0] for item in sorted_elements[:result_k]]
#
#     print(f"Исходный массив: {nums}, k={k} ")
#     print(most_common)
#
# massive_one()


def filtred_slov():


    dict1 = {
        1: {"name": "Иван", "age": 17},
        2: {"name": "Максим", "age": 27},
        3: {"name": "Петр", "age": 30}
    }

    dict2 = {
        2: {"name": "Мария", "age": 20},
        4: {"name": "Анна", "age": 22}
    }

    merged_dict = dict1.copy()
    merged_dict.update(dict2)


    result_dict = {}
    for user_id, data in merged_dict.items():
        if data["age"] >= 18:
            result_dict[user_id] = data

    print(result_dict)

filtred_slov()