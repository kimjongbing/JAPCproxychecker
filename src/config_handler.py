from src import directory_handler, get_proxy_sources_from_json, fetch_proxies

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
