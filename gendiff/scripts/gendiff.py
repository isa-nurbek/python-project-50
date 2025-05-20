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

    first_file = json.load(open(args.first_file))
    second_file = json.load(open(args.second_file))

    return first_file, second_file


def main():
    parse_file()


if __name__ == "__main__":
    main()
