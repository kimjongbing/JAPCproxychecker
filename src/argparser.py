import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Process files")
    parser.add_argument(
        "-i",
        "--input_file",
        dest="input_file_path",
        default="proxies.txt",
        help="Input file",
    )
    parser.add_argument(
        "-o",
        "--output_file",
        dest="output_file_path",
        default=None,
        help="Optional output file",
    )
    return parser.parse_args()
