import json


def get_format_json(diff):
    return json.dumps(diff, indent=4)
