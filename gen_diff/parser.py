from json import load as json_load
from yaml import safe_load as yaml_load


def parsing_file(path_file):
    format_file = path_file.split('.')[1]
    if format_file == "json":
        file = json_load(open(path_file))
    else:
        file = yaml_load(open(path_file))
    return file
