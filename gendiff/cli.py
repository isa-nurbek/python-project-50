import argparse


def parse_cli():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        help="set format of output",
        choices=["stylish", "plain", "json"],
        default="stylish",
    )
    args = parser.parse_args()

    return args.first_file, args.second_file, args.format
