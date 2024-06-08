import re


def clear_names(file_name: str) -> list:
    """ Функция для очистки имен от лишних символов """
    new_names_list = list()
    with open("../data/names.txt", "r", encoding="utf-8") as names_file:
        names_list = names_file.read().split()
        for name_item in names_list:
            new_name = ""
            for symbol in name_item:
                if symbol.isalpha():
                    new_name += symbol
            if new_name.isalpha():
                new_names_list.append(new_name)
    return new_names_list


def is_cyrilic(name_item: str) -> bool:
    """ Проверка на русские символы """

    return bool(re.search("[а-яА-Я]", name_item))

def filter_russian_names(names_list: list) -> list:
    """ Фильтрайия русских имен """
    new_names_list = list()
    for name_item in names_list:
        if is_cyrilic(name_item):
            new_names_list.append(name_item)
    return new_names_list


def filter_english_names(names_list: list) -> list:
    """ Фильтрайия английских имен """
    new_names_list = list()
    for name_item in names_list:
        if not is_cyrilic(name_item):
            new_names_list.append(name_item)
    return new_names_list


def save_to_file(file_name: str, data: str) -> None:
    """ Сохраняет данные в файл """
    with open("../data/russian_names.txt", "w", encoding="utf-8") as names_file:
        names_file.write(data)


def save_to_file_english(file_name: str, data: str) -> None:
    """ Сохраняет данные в файл """
    with open("../data/english_names.txt", "w", encoding="utf-8") as names_file:
        names_file.write(data)


if __name__ == "__main__":
    c_names = clear_names("names.txt")

    filtered_names = filter_russian_names(c_names)
    save_to_file("russian_names.txt", "\n".join(filtered_names))

    filtered_names = filter_english_names(c_names)
    save_to_file_english("english_names.txt", "\n".join(filtered_names))

