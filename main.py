from src import ProxyChecker, read_proxies_from_file, write_proxies_to_file


def main():
    proxies = read_proxies_from_file("http.txt")
    checker = ProxyChecker(proxies)
    good_proxies = checker.filter_proxies()
    write_proxies_to_file("http.txt", good_proxies)


if __name__ == "__main__":
    main()


# https://github.com/mertguvencli/http-proxy-list/blob/main/proxy-list/data.txt
