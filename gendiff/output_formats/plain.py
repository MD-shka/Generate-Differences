def format_plain_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    return value


def join_lines(diff):
    return "\n".join(diff)


def get_change(path_str,
               status,
               value
               ):
    if status == 'added':
        return f"{path_str} was added with value: {format_plain_value(value)}"
    elif status == 'deleted':
        return f"{path_str} was removed"
    elif status == 'changed':
        old_value = value[0]["value"]
        new_value = value[1]["value"]
        return (f"{path_str} was updated. From "
                f"{format_plain_value(old_value)} to "
                f"{format_plain_value(new_value)}")


def format_plain(diff, path_key=None):
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
        )
        if change:
            result.append(change)
        elif isinstance(changes.get('value'), dict):
            result.append(format_plain(changes['value'], current_path))
    return join_lines(result)
