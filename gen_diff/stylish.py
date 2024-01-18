SPECIAL_SYMBOLS = {"unchanged": "  ", "added": "+ ", "deleted": "- "}


def is_dict(value):
    return isinstance(value, dict)


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return value


def get_recursive_or_value(value, shift, key, indent, depth):
    pattern = f"{indent}{shift}{key}: "
    return (pattern + f"""{stylish(value, depth + 1)
            if is_dict(value)
            else format_value(value)}""")


def stylish(diff, depth=1):
    indent = ' ' * (depth * 4 - 2)
    result = []
    for key, changes in diff.items():
        if isinstance(changes, dict) and 'status' in changes:
            if changes['status'] in SPECIAL_SYMBOLS:
                result.append(
                    get_recursive_or_value(
                        changes['value'],
                        SPECIAL_SYMBOLS[changes['status']],
                        key,
                        indent,
                        depth
                    )
                )
            if 'old_value' in changes:
                result.append(
                    get_recursive_or_value(
                        changes['old_value'],
                        SPECIAL_SYMBOLS['deleted'],
                        key,
                        indent,
                        depth
                    )
                )
            if 'new_value' in changes:
                result.append(
                    get_recursive_or_value(
                        changes['new_value'],
                        SPECIAL_SYMBOLS['added'],
                        key,
                        indent,
                        depth
                    )
                )
        else:
            result.append(
                get_recursive_or_value(
                    changes,
                    SPECIAL_SYMBOLS['unchanged'],
                    key,
                    indent,
                    depth
                )
            )
    str_result = "\n".join(result)
    str_result = "{\n" + str_result + "\n" + indent[:-2] + "}"
    return str_result
