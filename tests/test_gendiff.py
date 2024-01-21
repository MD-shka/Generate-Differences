import json
import pytest
import gendiff.scripts.gendiff as gen_diff
from gendiff import parser


@pytest.mark.parametrize("path_first_file, path_second_file, diff_files, format_name", [
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'tests/fixtures/diff_file1_file2.md',
     'stylish'
     ),
    ('tests/fixtures/file1.yaml',
     'tests/fixtures/file2.yml',
     'tests/fixtures/diff_file1_file2.md',
     'stylish'
     ),
    ('tests/fixtures/file1.yaml',
     'tests/fixtures/file2.json',
     'tests/fixtures/diff_file1_file2.md',
     'stylish'
     ),
    ('tests/fixtures/nested_file1.json',
     'tests/fixtures/nested_file2.json',
     'tests/fixtures/diff_nested_file1_nested_file2.md',
     'stylish'
     ),
    ('tests/fixtures/nested_file1.yaml',
     'tests/fixtures/nested_file2.yml',
     'tests/fixtures/diff_nested_file1_nested_file2.md',
     'stylish'
     ),
    ('tests/fixtures/identical_nested_dictionaries_file1.json',
     'tests/fixtures/identical_nested_dictionaries_file2.yaml',
     'tests/fixtures/diff_identical_nested_dictionaries.md',
     'stylish'
     ),
    ('tests/fixtures/nested_file1.json',
     'tests/fixtures/nested_file2.yml',
     'tests/fixtures/result_gendiff_format_plain.md',
     'plain'
     ),
    ('tests/fixtures/nested_file1.json',
     'tests/fixtures/nested_file2.yml',
     'tests/fixtures/result_gendiff_format_json.json',
     'json'
     )
])
def test_generate_diff(path_first_file, path_second_file, diff_files, format_name):
    with open(diff_files, 'r') as file:
        result = file.read()
    diff = gen_diff.generate_diff(path_first_file, path_second_file, format_name)

    assert diff == result


def test_process_cmd(monkeypatch):
    monkeypatch.setattr('sys.argv', ['script.py', 'file1.json', 'file2.json'])
    result = gen_diff.process_cmd()
    assert result == ('file1.json', 'file2.json', 'stylish')


def test_main(monkeypatch):
    file1 = '{"key": "value"}'
    file2 = '{"key": "value"}'

    monkeypatch.setattr(parser, "parsing_file", lambda path: json.loads(file1) if path == "file1.json" else json.loads(
        file2))
    monkeypatch.setattr('sys.argv', ['script.py', 'file1.json', 'file2.json'])
    result = gen_diff.main()
    assert result == "{\n    key: value\n}"


if __name__ == '__main__':
    pytest.main([__file__])
