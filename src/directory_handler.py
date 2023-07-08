import os
import json


def get_config(json_file_path):
    with open(json_file_path, "r") as json_file:
        return json.load(json_file)


def get_full_file_path(file_path, default_directory):
    return os.path.join(default_directory, file_path)
