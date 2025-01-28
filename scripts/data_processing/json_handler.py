# -*- coding: utf-8 -*-

import json


def read_json(file_path):
    # JSON-file -> Python object
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json(file_path, json_data, indent=4):
    # Python object -> JSON-file
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=indent, ensure_ascii=False)


def pretty_print_json(json_data):
    print(json.dumps(json_data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    sample_data = {
        "name": "Alice",
        "age": 25,
        "skills": ["Python", "ML"]
    }

    write_json('sample.json', sample_data)

    read_data = read_json('sample.json')
    print(f"Read data type: {type(read_data)}")
    pretty_print_json(read_data)
