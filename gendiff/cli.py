import argparse


def parse_cli():
    # Create parser
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    
    # Add arguments
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f", "--format",
        help="set format of output",
        choices=["stylish", "plain", "json"],
        default="stylish"
    )
    
    # Parse arguments
    args = parser.parse_args()

    return args.first_file, args.second_file, args.format