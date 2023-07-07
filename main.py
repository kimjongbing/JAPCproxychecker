from src import ProxyChecker, read_proxies_from_file, write_proxies_to_file
from src import parse_args


def main(input_file_path, output_file_path):
    proxies = read_proxies_from_file(input_file_path)
    checker = ProxyChecker(proxies)
    good_proxies = checker.filter_proxies()
    if output_file_path:
        write_proxies_to_file(output_file_path, good_proxies)
    else:
        write_proxies_to_file(input_file_path, good_proxies)


if __name__ == "__main__":
    args = parse_args()
    main(args.input_file_path, args.output_file_path)
