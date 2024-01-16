#!/usr/bin/env python3
import argparse
from gen_diff import parser
from gen_diff import stylish


def generate_diff(first_file, second_file):
    keys = set(first_file.keys()) | set(second_file.keys())
    diff = []

    for key in sorted(keys):
        value_first = first_file.get(key)
        value_second = second_file.get(key)

        if value_first == value_second:
            diff.append((key, value_first, 'unchanged'))
        else:
            if value_first is not None:
                diff.append((key, value_first, 'deleted'))
            if value_second is not None:
                diff.append((key, value_second, 'added'))

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
    stylish_diff = '\n'.join(stylish.stylish(diff))
    return "{\n" + stylish_diff.lower() + "\n}"


if __name__ == '__main__':
    main()
