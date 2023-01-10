import csv


def read_file(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file, mode='r', encoding='utf-8') as file:
            return list(csv.reader(file))
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def write_file(content, path_to_file):
    try:
        with open("data/mkt_campaign.txt", mode="w") as analyze_log:
            analyze_log.write(content)
    except ValueError:
        raise ValueError


def get_unique_days(data):
    days = [row[2] for row in data]
    return list(set(days))


def get_unique_dish(data):
    data_dishes = [element[1] for element in data]
    return list(set(data_dishes))


def count_dish_by_customer(data, person):
    dish_count = dict()

    person_info = [row for row in data if row[0] == person]
    for row in person_info:
        if row[1] in dish_count:
            dish_count[row[1]] += 1
        else:
            dish_count[row[1]] = 1

    return dish_count

def analyze_log(path_to_file):
    raise NotImplementedError
