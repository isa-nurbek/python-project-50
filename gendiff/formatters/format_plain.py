def format_value(val):
    if isinstance(val, dict):
        return "[complex value]"
    if isinstance(val, bool):
        return "true" if val else "false"
    elif val is None:
        return "null"
    elif isinstance(val, (int, float)):
        return str(val)
    else:
        return f"'{str(val)}'"


def format_plain(diff: dict) -> str:
    def node_format(node, ancestry_name=""):
        result = []
        for key, value in node.items():
            proper_name = f"{ancestry_name}{key}"
            match value["status"]:
                case "added":
                    val = format_value(value["value"])
                    result.append(
                        f"Property '{proper_name}' was added with value: {val}"
                    )
                case "removed":
                    result.append(f"Property '{proper_name}' was removed")
                case "changed":
                    old_value = format_value(value["old_value"])
                    new_value = format_value(value["new_value"])
                    result.append(
                        f"Property '{proper_name}' was updated. From {old_value} to {new_value}"
                    )
                case "nested":
                    children = node_format(value["children"], f"{proper_name}.")
                    result.extend(children)
        return result

    lines = node_format(diff)
    return "\n".join(lines)
