#!/usr/bin/env python3
import argparse
from gen_diff import parser, stylish, build


def generate_diff(first_file, second_file, formater=stylish.stylish):
    diff = build.build_diff(first_file, second_file)
    result = formater(diff)
    return result


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
    return generate_diff(first_file, second_file)


if __name__ == '__main__':
    main()
