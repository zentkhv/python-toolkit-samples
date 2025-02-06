# -*- coding: utf-8 -*-

import os
import subprocess


def get_environment_variables():
    return os.environ


def execute_command(command):
    return os.system(command)


def execute_shell_command(command: str):
    result = subprocess.run(command, shell=True, capture_output=True)
    result = result.stdout.decode('utf-8')  # result.returncode
    return result


if __name__ == '__main__':
    print()
