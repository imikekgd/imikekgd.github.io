import json
import os
import functools


def get_directory_structure(root_dir):
    data = {}
    root_dir = root_dir.rstrip(os.sep)
    start = root_dir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(root_dir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = functools.reduce(dict.get, folders[:-1], data)
        parent[folders[-1]] = subdir
    return data


def parse():
    info = get_directory_structure(r'dos')
    json_info = json.dumps(info)

    with open(r'assets\info.js', 'w') as f:
        f.write('dosstructure = ' + json_info)


if __name__ == "__main__":
    parse()
