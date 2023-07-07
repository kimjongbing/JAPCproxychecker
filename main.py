from src import (
    ProxyChecker, 
    read_proxies_from_file, 
    write_proxies_to_file, 
    parse_args, 
    get_proxy_sources_from_json, 
    fetch_proxies, 
    directory_handler
)


def handle_config(json_file_path):
    if json_file_path:
        config = directory_handler.get_config(json_file_path)
        proxy_sources = get_proxy_sources_from_json(json_file_path)
        proxies = fetch_proxies(proxy_sources)
        default_input_directory = config.get('default_input_directory', '.')
        default_output_directory = config.get('default_output_directory', '.')
    else:
        default_input_directory = '.'
        default_output_directory = '.'
        proxies = None

    return default_input_directory, default_output_directory, proxies


def handle_file_paths(input_file_path, output_file_path, default_input_directory, default_output_directory):
    full_input_path = directory_handler.get_full_file_path(input_file_path, default_input_directory)
    full_output_path = directory_handler.get_full_file_path(output_file_path, default_output_directory)

    return full_input_path, full_output_path


def handle_proxies(full_input_path, proxies):
    if not proxies:
        proxies = read_proxies_from_file(full_input_path)
    
    checker = ProxyChecker(proxies)
    good_proxies = checker.filter_proxies()

    return good_proxies


def main(input_file_path, output_file_path, json_file_path):
    default_input_directory, default_output_directory, proxies = handle_config(json_file_path)
    full_input_path, full_output_path = handle_file_paths(input_file_path, output_file_path, default_input_directory, default_output_directory)
    good_proxies = handle_proxies(full_input_path, proxies)

    if output_file_path:
        write_proxies_to_file(full_output_path, good_proxies)
    else:
        write_proxies_to_file(full_input_path, good_proxies)


if __name__ == "__main__":
    args = parse_args()
    main(args.input_file_path, args.output_file_path, args.json_file_path)
