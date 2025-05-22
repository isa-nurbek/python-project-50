import json


def format_json(diff):
    """
    Format the diff dictionary as a JSON string.
    """
    return json.dumps(diff, indent=2)
