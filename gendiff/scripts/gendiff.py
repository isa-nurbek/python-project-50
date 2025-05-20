import argparse
import json


def generate_diff(first_file_path, second_file_path):
    try:
        with open(first_file_path) as f1, open(second_file_path) as f2:
            dict1 = json.load(f1)
            dict2 = json.load(f2)

        # Get all unique keys sorted alphabetically
        all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))

        # Build diff string
        lines = ["{"]
        for key in all_keys:
            if key in dict1 and key in dict2:
                if dict1[key] == dict2[key]:
                    lines.append(f"    {key}: {json.dumps(dict1[key])}")
                else:
                    lines.append(f"  - {key}: {json.dumps(dict1[key])}")
                    lines.append(f"  + {key}: {json.dumps(dict2[key])}")
            elif key in dict1:
                lines.append(f"  - {key}: {json.dumps(dict1[key])}")
            else:
                lines.append(f"  + {key}: {json.dumps(dict2[key])}")
        lines.append("}")

        return "\n".join(lines)
    except FileNotFoundError as e:
        print(f"Error: Could not find file - {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        help="set format of output",
    )

    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    if diff:
        print(diff)
