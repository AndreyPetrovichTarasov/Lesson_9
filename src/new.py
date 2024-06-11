# Написать функцию, которая принимает список словарей,
# содержащих информацию о студентах (имя, возраст, оценки)
# и возвращает список студентов, отсортированных по среднему баллу по убыванию.
# Если у студентов одинаковый средний балл,
# сортировать их по имени в алфавитном порядке.
# Пример ввода:
# [    {"name": "Alice", "age": 20, "grades": [90, 95, 85]},
#     {"name": "Bob", "age": 22, "grades": [85, 85, 85]},
#     {"name": "Charlie", "age": 21, "grades": [90, 95, 85]}
# ]
# Пример вывода:
# [    {"name": "Alice", "age": 20, "grades": [90, 95, 85]},
#     {"name": "Charlie", "age": 21, "grades": [90, 95, 85]},
#     {"name": "Bob", "age": 22, "grades": [85, 85, 85]}
# ]


from typing import List

list_students_main = [
    {"name": "Alice", "age": 20, "grades": [90, 95, 85]},
    {"name": "Bob", "age": 22, "grades": [85, 85, 85]},
    {"name": "Charlie", "age": 21, "grades": [90, 95, 85]}
]


def sorting_list_students(list_students: List) -> List:
    list_sorted = sorted(list_students, key=lambda x: (sum(x["grades"])/len(x["grades"])),reverse=True)

    return list_sorted


print(sorting_list_students(list_students_main))
