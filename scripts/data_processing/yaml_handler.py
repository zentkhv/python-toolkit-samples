# -*- coding: utf-8 -*-

import yaml


def read_yaml(file_path):
    # YAML-file -> Python object
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)


def write_yaml(file_path, yaml_data):
    # Python object -> YAML-file
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.safe_dump(yaml_data, file, allow_unicode=True, default_flow_style=False)


def pretty_print_yaml(yaml_data):
    print(yaml.safe_dump(yaml_data, allow_unicode=True, default_flow_style=False))


if __name__ == "__main__":
    sample_data = {
        "name": "Bob",
        "age": 30,
        "skills": ["Django", "DevOps"],
        "details": {"city": "New York", "experience": 5}
    }

    write_yaml('sample.yaml', sample_data)

    read_data = read_yaml('sample.yaml')
    print(f"Read data type: {type(read_data)}")
    pretty_print_yaml(read_data)
