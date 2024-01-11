import os
from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    local_path = '/home/project_gendiff/python-project-50'
    path_first_file = os.path.join(local_path, 'tests/fixtures/file1.json')
    path_second_file = os.path.join(local_path, 'tests/fixtures/file2.json')
    diff = ("{\n  - follow: False\n    host: hexlet.io\n"
            "  - proxy: 123.234.53.22\n  - timeout: 50\n"
            "  + timeout: 20\n  + verbose: True\n}")
    assert generate_diff(path_first_file, path_second_file) == diff