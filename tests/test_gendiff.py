import pytest
from gendiff.scripts import gendiff


@pytest.mark.parametrize("path_first_file, path_second_file, diff_files", [
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'tests/fixtures/diff_file1_file2.md'
     ),
])
def test_generate_diff(path_first_file, path_second_file, diff_files):
    with open(diff_files, 'r') as file:
        result = file.read()
    assert gendiff.generate_diff(path_first_file, path_second_file) == result


@pytest.fixture
def test_args(monkeypatch):
    monkeypatch.setattr('sys.argv', ['script.py', 'file1.json', 'file2.json'])
    return ('file1.json', 'file2.json')


def test_process_cmd(test_args):
    result = gendiff.process_cmd()
    assert result == test_args


def test_main(test_args, monkeypatch):
    monkeypatch.setattr('gendiff.scripts.gendiff.process_cmd', lambda: test_args)
    monkeypatch.setattr('gendiff.scripts.gendiff.generate_diff', lambda *args: '{}')
    result = gendiff.main()
    assert result == '{}'
