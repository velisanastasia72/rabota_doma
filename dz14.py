
multiply_three = lambda a, b, c: a * b * c

print(multiply_three(2, 5, 5))



students = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98}
]

print(sorted(students, key=lambda x: x['name']))

print(sorted(students, key=lambda x: x['final'], reverse=True))







students = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98}
]


print(max(students, key=lambda x: x['final']))


print(min(students, key=lambda x: x['final']))





nums = [3, 5, 7, 3, 9, 5, 7, 2]

square = lambda x: x ** 2
cube = lambda x: x ** 3


print(list(map(square, nums)))
print(list(map(cube, nums)))




