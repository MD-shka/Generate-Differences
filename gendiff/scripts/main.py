#!/usr/bin/env python3
from gendiff import generate_diff, parse_args


def main():
    path_first_file, path_second_file, format_name = parse_args.parse_args()
    print(
        generate_diff.generate_diff(
            path_first_file,
            path_second_file,
            format_name)
    )


if __name__ == '__main__':
    main()
