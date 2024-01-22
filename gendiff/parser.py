from json import loads as json_load
from yaml import safe_load as yaml_load


def read_file(path_file):
    with open(path_file, 'r') as file:
        file_content = file.read()
    return file_content


def parse_file(path_file):
    file_content = read_file(path_file)
    format_file = path_file.split('.')[1]
    if format_file == "json":
        return json_load(file_content)
    elif format_file in ("yaml", "yml"):
        return yaml_load(file_content)
    raise ValueError('Wrong format, use ".json", ".yaml" or ".yml"')
