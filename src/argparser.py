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

    parser.add_argument(
        "-j",
        "--proxy_sources_file",
        dest="json_file_path",
        default=None,
        help="Json file that has the proxy sources urls",
    )

    parser.add_argument(
        "-s",
        "--scheme",
        dest="proxy_scheme",
        default=None,
        help="Scheme to use for the proxies. If specified only this scheme is used. If not specified, every scheme will be attempted per proxy.",
    )
    return parser.parse_args()
