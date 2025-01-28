# -*- coding: utf-8 -*-

import os


def get_environment_variables():
    return os.environ

def execute_command(command):
    return os.system(command)


if __name__ == '__main__':
    print()