import json


def get_format_json(diff):
    print(json.dumps(diff, indent=4))
