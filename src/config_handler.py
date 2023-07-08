import json
from src.proxy_handler import ProxyHandler
from src.file_handler import FileHandler


class ConfigHandler:
    @staticmethod
    def get_config(json_file_path):
        with open(json_file_path, "r") as json_file:
            return json.load(json_file)

    @staticmethod
    def handle_config(json_file_path):
        if json_file_path:
            config = ConfigHandler.get_config(json_file_path)
            proxy_sources = FileHandler.get_proxy_sources_from_json(json_file_path)
            proxies = ProxyHandler.fetch_proxies(proxy_sources)
            default_input_directory = config.get("default_input_directory", ".")
            default_output_directory = config.get("default_output_directory", ".")
        else:
            default_input_directory = "."
            default_output_directory = "."
            proxies = None

        return default_input_directory, default_output_directory, proxies
