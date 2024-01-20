from gen_diff.build import is_dict


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif is_dict(value):
        return "[complex value]"
    return f"'{value}'"


def get_str_diff(diff):
    return "\n".join(diff)


def plain(diff, path_key=None):
    result = []
    if path_key is None:
        path_key = []
    for key, changes in diff.items():
        current_path = path_key + [key]
        path_str = f"Property '{'.'.join(current_path)}'"
        if is_dict(changes) and 'status' in changes:
            if changes['status'] == 'added':
                result.append(f"{path_str} was added with value: "
                              f"{format_value(changes['value'])}")
            elif changes['status'] == 'deleted':
                result.append(f"{path_str} was removed")
            elif is_dict(changes.get('value')):
                result.append(plain(changes['value'], current_path))
            elif 'old_value' in changes and 'new_value' in changes:
                result.append(f"{path_str} was updated. From "
                              f"{format_value(changes['old_value'])} to "
                              f"{format_value(changes['new_value'])}")
    return get_str_diff(result)
