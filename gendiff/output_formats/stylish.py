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


def get_stylish_join_lines(diff, depth):
    str_diff = "\n".join(diff)
    return "{\n" + str_diff + "\n" + get_indent(depth)[:-2] + "}"


def format_line(key, changes_value, depth, shift=SHIFTS["unchanged"]):
    pattern = f"{get_indent(depth)}{shift}{key}: "
    value = f"{format_value(changes_value, depth)}"
    line = pattern + value
    return line


def format_stylish(diff, depth=1):
    result = []
    for key, changes in diff.items():
        if isinstance(changes, dict) and 'status' in changes:
            status = changes['status']

            if status in SHIFTS:
                result.append(
                    format_line(
                        key,
                        changes["value"],
                        depth,
                        SHIFTS[status]
                    )
                )

            elif status == "changed":
                for change in changes["value"]:
                    result.append(
                        format_line(
                            key,
                            change["value"],
                            depth,
                            SHIFTS[change["status"]]
                        )
                    )

        else:
            result.append(format_line(key, changes, depth))

    return get_stylish_join_lines(result, depth)
