from gendiff.output_formats import stylish, plain, json
from gendiff import parser, build

FORMATS = {
    "stylish": stylish.format_stylish,
    "plain": plain.format_plain,
    "json": json.format_json
}


def generate_diff(path_first_file, path_second_file, format_name='stylish'):
    first_file = parser.parse_file(path_first_file)
    second_file = parser.parse_file(path_second_file)
    diff = build.build_diff(first_file, second_file)
    result = FORMATS[format_name](diff)
    return result
