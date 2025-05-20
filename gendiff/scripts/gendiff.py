import argparse
import json


def parse_file():
    # Create parser
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    # Add arguments
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        help="set format of output",
    )

    # Parse arguments
    args = parser.parse_args()

    try:
        with open(args.first_file) as f1, open(args.second_file) as f2:
            first_file = json.load(f1)
            second_file = json.load(f2)
        return first_file, second_file
    except FileNotFoundError as e:
        print(f"Error: Could not find file - {e}")
        return None, None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
        return None, None


def main():
    first_file, second_file = parse_file()
    if first_file is not None and second_file is not None:
        print("Files parsed successfully!")


if __name__ == "__main__":
    main()
