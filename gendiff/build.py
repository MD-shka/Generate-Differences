def build_diff(file1_content, file2_content):
    diff = {}

    for key in sorted(set(file1_content.keys()) | set(file2_content.keys())):
        value1 = file1_content.get(key)
        value2 = file2_content.get(key)

        if isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = {
                "status": "nested",
                "value": build_diff(value1, value2)
            }
        elif value1 == value2:
            diff[key] = {
                "status": "unchanged",
                "value": value1
            }
        elif key not in file2_content:
            diff[key] = {
                "status": "deleted",
                "value": value1
            }
        elif key not in file1_content:
            diff[key] = {
                "status": "added",
                "value": value2
            }
        else:
            diff[key] = {
                "status": "changed",
                "old_value": value1,
                "new_value": value2
            }
    return diff
