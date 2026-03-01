
import json
import os


def ensure_directory(path):
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)


def read_json(path):

    if not os.path.exists(path):
        return {}

    with open(path, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except:
            return {}


def write_json(path, data):

    ensure_directory(path)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)