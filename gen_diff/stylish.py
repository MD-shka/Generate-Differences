def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return value


def stylish(diff, depth=1):
    indent = ' ' * (depth * 4 - 2)
    result = []
    for key, changes in diff.items():
        if isinstance(changes, dict) and 'status' in changes:
            status = changes['status']
            if status == 'unchanged':
                if isinstance(changes['value'], dict):
                    result.append(f"{indent}  {key}: "
                                  f"{stylish(changes['value'], depth + 1)}")
                else:
                    result.append(f"{indent}  {key}: "
                                  f"{format_value(changes['value'])}")
            elif status == 'deleted':
                if isinstance(changes['value'], dict):
                    result.append(f"{indent}- {key}: "
                                  f"{stylish(changes['value'], depth + 1)}")
                else:
                    result.append(f"{indent}- {key}: "
                                  f"{format_value(changes['value'])}")
            elif status == 'added':
                if isinstance(changes['value'], dict):
                    result.append(f"{indent}+ {key}: "
                                  f"{stylish(changes['value'], depth + 1)}")
                else:
                    result.append(f"{indent}+ {key}: "
                                  f"{format_value(changes['value'])}")
            elif status == 'changed':
                if 'old_value' in changes:
                    if isinstance(changes['old_value'], dict):
                        result.append(f"{indent}- {key}: "
                                      f"{stylish(changes['old_value'], depth + 1)}")
                    else:
                        result.append(f"{indent}- {key}: "
                                      f"{format_value(changes['old_value'])}")
                if 'new_value' in changes:
                    if isinstance(changes['new_value'], dict):
                        result.append(f"{indent}+ {key}: "
                                      f"{stylish(changes['new_value'], depth + 1)}")
                    else:
                        result.append(f"{indent}+ {key}: "
                                      f"{format_value(changes['new_value'])}")
        else:
            if isinstance(changes, dict):
                result.append(f"{indent}  {key}: "
                              f"{stylish(changes, depth + 1)}")
            else:
                result.append(f"{indent}  {key}: {format_value(changes)}")
    str_result = "\n".join(result)
    str_result = "{\n" + str_result + "\n" + indent[:-2] + "}"
    return str_result
