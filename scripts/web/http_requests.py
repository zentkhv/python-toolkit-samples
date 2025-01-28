# -*- coding: utf-8 -*-

import requests


def get_request(url, params=None):
    response = requests.get(url, params=params)
    return response.json()

def post_request(url, json_data=None):
    response = requests.post(url, json=json_data)
    return response.json()

if __name__ == '__main__':
    test_data = get_request('https://jsonplaceholder.typicode.com/posts')
    print(test_data)
