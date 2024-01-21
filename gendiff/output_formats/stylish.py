from build import is_dict


SPECIAL_SYMBOLS = {"unchanged": "  ", "added": "+ ", "deleted": "- "}


def get_indent(depth):
    return ' ' * (depth * 4 - 2)


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return value


def get_recursive_or_value(
        value,
        shift,
        key=SPECIAL_SYMBOLS["unchanged"],
        depth=1
):
    pattern = f"{get_indent(depth)}{shift}{key}: "
    return (pattern + f"""{stylish(value, depth + 1)
            if is_dict(value)
            else format_value(value)}""")


def get_str_stylish_diff(diff, depth):
    str_diff = "\n".join(diff)
    return "{\n" + str_diff + "\n" + get_indent(depth)[:-2] + "}"


def stylish(diff, depth=1):
    result = []
    for key, changes in diff.items():
        if is_dict(changes) and 'status' in changes:
            if changes['status'] in SPECIAL_SYMBOLS:
                result.append(
                    get_recursive_or_value(
                        changes['value'],
                        SPECIAL_SYMBOLS[changes['status']],
                        key,
                        depth
                    )
                )
            if 'old_value' in changes:
                result.append(
                    get_recursive_or_value(
                        changes['old_value'],
                        SPECIAL_SYMBOLS['deleted'],
                        key,
                        depth
                    )
                )
            if 'new_value' in changes:
                result.append(
                    get_recursive_or_value(
                        changes['new_value'],
                        SPECIAL_SYMBOLS['added'],
                        key,
                        depth
                    )
                )
        else:
            result.append(
                get_recursive_or_value(
                    changes,
                    SPECIAL_SYMBOLS['unchanged'],
                    key,
                    depth
                )
            )
    return get_str_stylish_diff(result, depth)
