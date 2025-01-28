# -*- coding: utf-8 -*-

import os


def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def create_directory(path):
    os.makedirs(path, exist_ok=True)


if __name__ == '__main__':
    create_directory("a")
