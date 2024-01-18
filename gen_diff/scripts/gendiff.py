#!/usr/bin/env python3
import argparse
from gen_diff import parser, stylish


def generate_diff(dict1, dict2):
    diff = {}

    for key in sorted(set(dict1.keys()) | set(dict2.keys())):
        value1 = dict1.get(key)
        value2 = dict2.get(key)

        if value1 == value2:
            if isinstance(value1, dict):
                nested_diff = generate_diff(value1, value2)
                if nested_diff:
                    diff[key] = {
                        'status': 'unchanged',
                        'value': nested_diff
                    }
            else:
                diff[key] = {
                    'status': 'unchanged',
                    'value': value1
                }
        elif key in dict1 and key not in dict2:
            diff[key] = {
                'status': 'deleted',
                'value': value1
            }
        elif key not in dict1 and key in dict2:
            diff[key] = {
                'status': 'added',
                'value': value2
            }
        elif value1 != value2:
            if isinstance(value1, dict) and isinstance(value2, dict):
                nested_diff = generate_diff(value1, value2)
                diff[key] = {
                    'status': 'unchanged',
                    'value': nested_diff
                }
            else:
                diff[key] = {
                    'status': 'changed',
                    'old_value': value1,
                    'new_value': value2
                }
    return diff


def process_cmd():
    pars = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    pars.add_argument("-f", "--format", help="set format of output")
    pars.add_argument("first_file")
    pars.add_argument("second_file")
    args = pars.parse_args()

    return args.first_file, args.second_file


def main():
    path_first_file, path_second_file = process_cmd()
    first_file = parser.parsing_file(path_first_file)
    second_file = parser.parsing_file(path_second_file)
    diff = generate_diff(first_file, second_file)
    return stylish.stylish(diff)


if __name__ == '__main__':
    main()
