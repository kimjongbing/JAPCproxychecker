import json

def read_json_file(json_file_path):
    with open(json_file_path, 'r') as json_file:
        return json.load(json_file)

def get_proxy_sources_from_json(json_file_path):
    data = read_json_file(json_file_path)
    return data["sources"]