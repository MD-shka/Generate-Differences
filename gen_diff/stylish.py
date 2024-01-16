def stylish(diff, depth=1):
    indent = "  " * depth
    stylish_diff = []

    for key, value, change in diff:
        if change == "unchanged":
            stylish_diff.append(f"{indent}  {key}: {value}")
        elif change == "deleted":
            stylish_diff.append(f"{indent}- {key}: {value}")
        elif change == "added":
            stylish_diff.append(f"{indent}+ {key}: {value}")
        stylish_diff.extend(stylish(value, depth + 1) if
                            isinstance(value, list) else [])

    return stylish_diff
