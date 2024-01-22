SHIFTS = {
    "nested": "  ",
    "unchanged": "  ",
    "added": "+ ",
    "deleted": "- "
}


def get_indent(depth):
    return ' ' * (depth * 4 - 2)


def format_value(value, depth):
    if isinstance(value, dict):
        return format_stylish(value, depth + 1)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return value


def get_recursive_or_value(
        value,
        key,
        depth=1,
        shift='  '
):
    pattern = f"{get_indent(depth)}{shift}{key}: "
    return pattern + f"{format_value(value, depth)}"


def stylish_join_lines(diff, depth):
    str_diff = "\n".join(diff)
    return "{\n" + str_diff + "\n" + get_indent(depth)[:-2] + "}"


def format_stylish(diff, depth=1):
    result = []
    for key, changes in diff.items():
        if isinstance(changes, dict) and 'status' in changes:
            status = changes['status']

            if status in SHIFTS:
                pattern = f"{get_indent(depth)}{SHIFTS[status]}{key}: "
                value = f"{format_value(changes['value'], depth)}"
                result.append(pattern + value)

            elif status == "changed":
                pattern = f"{get_indent(depth)}{SHIFTS['deleted']}{key}: "
                value = f"{format_value(changes['old_value'], depth)}"
                result.append(pattern + value)

                pattern = f"{get_indent(depth)}{SHIFTS['added']}{key}: "
                value = f"{format_value(changes['new_value'], depth)}"
                result.append(pattern + value)

        else:
            pattern = f"{get_indent(depth)}  {key}: "
            value = f"{format_value(changes, depth)}"
            result.append(pattern + value)

    return stylish_join_lines(result, depth)
