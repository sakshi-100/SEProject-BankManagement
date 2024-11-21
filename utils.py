import json

def read_data(filepath):
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def write_data(filepath, data):
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)
