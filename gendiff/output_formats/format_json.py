import json


def get_format_json(diff):
    format_json = json.dumps(diff, indent=4)
    print(format_json)
    return format_json
