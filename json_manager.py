import json
import os

def read_json():
    if not os.path.isfile('data.json'):
        with open('data.json', 'w') as f:
            json.dump([], f)
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data


def write_json(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)

__all__ = ['read_json', 'write_json']