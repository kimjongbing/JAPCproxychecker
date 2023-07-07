from src import ProxyChecker, read_proxies_from_file, write_proxies_to_file, parse_args, fetch_proxies, get_proxy_sources_from_json


def main(input_file_path, output_file_path, json_file_path):
    if json_file_path:
        proxy_sources = get_proxy_sources_from_json(json_file_path)
        proxies = fetch_proxies(proxy_sources)
    else:
        proxies = read_proxies_from_file(input_file_path)
        
    checker = ProxyChecker(proxies)
    good_proxies = checker.filter_proxies()
    if output_file_path:
        write_proxies_to_file(output_file_path, good_proxies)
    else:
        write_proxies_to_file(input_file_path, good_proxies)


if __name__ == "__main__":
    args = parse_args()
    main(args.input_file_path, args.output_file_path, args.json_file_path)
