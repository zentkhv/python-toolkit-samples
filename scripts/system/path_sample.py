# -*- coding: utf-8 -*-

import os


if __name__ == '__main__':
    file_path = os.path.abspath(__file__)
    file_dir  = os.path.dirname(file_path)
    join_dir = os.path.join(file_dir, 'test-dir')

    print(f"file_path = {file_path}")
    print(f"file_dir  = {file_dir}")
    print(f"join_dir  = {join_dir}")