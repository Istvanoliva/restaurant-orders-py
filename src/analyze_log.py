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


def favorite_dish(data):
    dish_count = count_dish_by_customer(data, 'maria')
    return max(dish_count, key=dish_count.get)


def count_requested_hamburguer_by_arnaldo(data):
    dish_count = count_dish_by_customer(data, 'arnaldo')
    return dish_count['hamburguer']


def dish_never_requested(data):
    unique_foods = get_unique_dish(data)
    joao_food_count = count_dish_by_customer(data, 'joao')
    dish_never_requested = set(
      [food for food in unique_foods if food not in joao_food_count.keys()]
    )
    return dish_never_requested

def analyze_log(path_to_file):
    raise NotImplementedError
