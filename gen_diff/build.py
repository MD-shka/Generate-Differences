def build_diff(data1, data2):
    diff = {}

    for key in sorted(set(data1.keys()) | set(data2.keys())):
        value1 = data1.get(key)
        value2 = data2.get(key)

        if value1 == value2:
            if isinstance(value1, dict):
                nested_diff = build_diff(value1, value2)
                if nested_diff:
                    diff[key] = {
                        'status': 'unchanged',
                        'value': nested_diff
                    }
            else:
                diff[key] = {
                    'status': 'unchanged',
                    'value': value1
                }
        elif key in data1 and key not in data2:
            diff[key] = {
                'status': 'deleted',
                'value': value1
            }
        elif key not in data1 and key in data2:
            diff[key] = {
                'status': 'added',
                'value': value2
            }
        elif value1 != value2:
            if isinstance(value1, dict) and isinstance(value2, dict):
                nested_diff = build_diff(value1, value2)
                diff[key] = {
                    'status': 'unchanged',
                    'value': nested_diff
                }
            else:
                diff[key] = {
                    'status': 'changed',
                    'old_value': value1,
                    'new_value': value2
                }
    return diff
