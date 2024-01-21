from gendiff.build import is_dict


def format_plain_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif is_dict(value):
        return "[complex value]"
    return f"'{value}'"


def get_str_diff(diff):
    return "\n".join(diff)


def get_change(path_str,
               status,
               value=None,
               old_value=None,
               new_value=None
               ):
    if status == 'added':
        return f"{path_str} was added with value: {format_plain_value(value)}"
    elif status == 'deleted':
        return f"{path_str} was removed"
    elif status == 'changed':
        return (f"{path_str} was updated. From "
                f"{format_plain_value(old_value)} to "
                f"{format_plain_value(new_value)}")


def plain(diff, path_key=None):
    result = []
    if path_key is None:
        path_key = []

    for key, changes in diff.items():
        current_path = path_key + [key]
        path_str = f"Property '{'.'.join(current_path)}'"
        change = get_change(
            path_str,
            changes['status'],
            changes.get('value'),
            changes.get('old_value'),
            changes.get('new_value')
        )
        if change:
            result.append(change)
        elif is_dict(changes.get('value')):
            result.append(plain(changes['value'], current_path))
    return get_str_diff(result)