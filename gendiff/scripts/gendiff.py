import argparse


def main():
    # Create parser
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    
    # Add arguments
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    
    parser.parse_args()


if __name__ == '__main__':
    main()