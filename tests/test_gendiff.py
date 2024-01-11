from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    assert generate_diff(
        "python-project-50/tests/fixtures/file1.json",
        "python-project-50/tests/fixtures/file2.json"
    ) == ("{\n  - follow: False\n    host: hexlet.io\n  - proxy: 123.234.53.22\n"
          "  - timeout: 50\n  + timeout: 20\n  + verbose: True\n}")