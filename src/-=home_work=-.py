# Напишите функцию, которая принимает на вход список словарей и значение для ключа
# state (опциональный параметр со значением по умолчанию EXECUTED) и возвращает новый список,
# содержащий только те словари, у которых ключ state содержит переданное в функцию значение.
#
# Вход функции
# [
#     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
#     ]
#
# # Выход функции со статусом по умолчанию EXECUTED
# [
#     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
#     ]
#
# # Выход функции, если вторым аргументов передано 'CANCELED'
# [
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
#     ]

from typing import List, Dict


def filter_by_state(list_id: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    sorted_list_id = [dict_id for dict_id in list_id if dict_id["state"] == state]
    return sorted_list_id


print(filter_by_state([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
], state="CANCELED"))


# Напишите функцию, которая принимает на вход список словарей и возвращает новый список,
# в котором исходные словари отсортированы по убыванию даты (ключ date).
# Функция принимает два аргумента, второй необязательный задает порядок сортировки (убывание, возрастание).


def sort_by_date(list_id: List[Dict], reverse: bool = False) -> List[Dict]:
    sorted_list = sorted(list_id, key=lambda dict_id: dict_id["date"], reverse=reverse)
    return sorted_list


print(sort_by_date([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
], True))
