import json
import os
import yaml


def parse_file(file_path):
    _, ext = os.path.splitext(file_path)
    with open(file_path, "r") as f:
        if ext == ".json":
            return json.load(f)
        else:
            return yaml.safe_load(f)


def parse_files(file_path1, file_path2):
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)
    return file1, file2
