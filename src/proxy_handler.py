from src import ProxyChecker, read_proxies_from_file


def handle_proxies(full_input_path, proxies):
    if not proxies:
        proxies = read_proxies_from_file(full_input_path)

    checker = ProxyChecker(proxies)
    good_proxies = checker.filter_proxies()

    return good_proxies
