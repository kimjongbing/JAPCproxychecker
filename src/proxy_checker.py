import requests
import concurrent.futures
from urllib.parse import urlparse
from .counter import Counter


class ProxyChecker:
    def __init__(self, proxies, scheme=None):
        self.proxies = proxies
        self.scheme = scheme
        self.total_proxies = len(proxies)
        self.counter = Counter()

    def get_schemes(self, parsed_proxy):
        if parsed_proxy.scheme:
            return [parsed_proxy.scheme + "://"]
        elif self.scheme:
            return [self.scheme + "://"]
        else:
            return ["http://", "https://", "socks5://", "socks4://"]

    def format_proxy(self, scheme, proxy, parsed_proxy):
        if parsed_proxy.scheme:
            return proxy
        else:
            return scheme + proxy

    def get_response(self, formatted_proxy):
        proxies = {"http": formatted_proxy, "https": formatted_proxy}
        try:
            return requests.get("http://google.com", proxies=proxies, timeout=5)
        except (
            requests.exceptions.RequestException,
            requests.exceptions.ConnectTimeout,
            requests.exceptions.ReadTimeout,
        ):
            return None

    def check_proxy(self, proxy):
        parsed_proxy = urlparse(proxy)
        schemes = self.get_schemes(parsed_proxy)
        status = None

        for scheme in schemes:
            formatted_proxy = self.format_proxy(scheme, proxy, parsed_proxy)
            response = self.get_response(formatted_proxy)

            if response is not None and response.status_code == 200:
                print(f"Proxy {proxy} is good with {scheme[:-3]} scheme.")
                status = 200
            else:
                print(
                    f"Proxy {proxy} failed with status code {status} for {scheme} scheme."
                )

            self.counter.increment()
            print((f"Checked {self.counter.value()} out of {self.total_proxies}"))

            return proxy if status == 200 else None

    def filter_proxies(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
            return list(filter(None, executor.map(self.check_proxy, self.proxies)))
