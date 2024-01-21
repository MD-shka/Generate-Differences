#!/usr/bin/env python3
import argparse


from gendiff import parser, build
from gendiff.output_formats import stylish, plain, format_json


def generate_diff(path_first_file, path_second_file, format_name='stylish'):
    first_file = parser.parsing_file(path_first_file)
    second_file = parser.parsing_file(path_second_file)
    formats = {
        "stylish": stylish.stylish,
        "plain": plain.plain,
        "json": format_json.get_format_json
    }
    diff = build.build_diff(first_file, second_file)
    result = formats[format_name](diff)
    print(result)


def process_cmd():
    pars = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    pars.add_argument(
        "-f", "--format",
        help="set format of output",
        choices=["stylish", "plain", "json"],
        default="stylish"
    )
    pars.add_argument("first_file")
    pars.add_argument("second_file")
    args = pars.parse_args()

    return args.first_file, args.second_file, args.format


def main():
    path_first_file, path_second_file, format_name = process_cmd()
    return generate_diff(path_first_file, path_second_file, format_name)


if __name__ == '__main__':
    main()
