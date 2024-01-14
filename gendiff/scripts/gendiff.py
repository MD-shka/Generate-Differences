#!/usr/bin/env python3
import argparse
from gendiff.parser import parsing_file


def generate_diff(path_first_file, path_second_file):
    diff = {}
    first_file = parsing_file(path_first_file)
    second_file = parsing_file(path_second_file)
    keys = set(first_file.keys()) | set(second_file.keys())

    for key in sorted(keys):
        value_first_file = first_file.get(key)
        value_second_file = second_file.get(key)

        if value_first_file == value_second_file:
            diff[f"  {key}"] = value_first_file
        else:
            if value_first_file is not None:
                diff[f"- {key}"] = value_first_file
            if value_second_file is not None:
                diff[f"+ {key}"] = value_second_file

    formatted_diff = '\n'.join(
        [f'  {key}: {value}' for key, value in diff.items()]
    )

    return '{\n' + formatted_diff.lower() + '\n}'


def process_cmd():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("-f", "--format", help="set format of output")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()

    return args.first_file, args.second_file


def main():
    path_first_file, path_second_file = process_cmd()
    return generate_diff(path_first_file, path_second_file)


if __name__ == '__main__':
    main()
