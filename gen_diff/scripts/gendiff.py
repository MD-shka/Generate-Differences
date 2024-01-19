#!/usr/bin/env python3
import argparse
from gen_diff import parser, build
from gen_diff.output_formats import stylish, plain


def generate_diff(first_file, second_file, format_name):
    formats = {"stylish": stylish.stylish, "plain": plain.plain}
    diff = build.build_diff(first_file, second_file)
    result = formats[format_name](diff)
    return result


def process_cmd():
    pars = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    pars.add_argument(
        "-f", "--format",
        help="set format of output",
        choices=["stylish", "plain"],
        default="stylish"
    )
    pars.add_argument("first_file")
    pars.add_argument("second_file")
    args = pars.parse_args()

    return args.first_file, args.second_file, args.format


def main():
    path_first_file, path_second_file, format_name = process_cmd()
    first_file = parser.parsing_file(path_first_file)
    second_file = parser.parsing_file(path_second_file)
    return generate_diff(first_file, second_file, format_name)


if __name__ == '__main__':
    main()
