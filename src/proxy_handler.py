from src.proxy_checker import ProxyChecker
from src.file_handler import FileHandler


def handle_proxies(full_input_path, proxies):
    if not proxies:
        proxies = FileHandler.read_from_file(full_input_path)

    checker = ProxyChecker(proxies)
    good_proxies = checker.filter_proxies()

    return good_proxies
