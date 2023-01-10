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


def analyze_log(path_to_file):
    raise NotImplementedError
