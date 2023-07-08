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

    def check_proxy(self, proxy):
        print(f"Checking proxy: {proxy}")
        parsed_proxy = urlparse(proxy)
        if parsed_proxy.scheme:
            schemes = [parsed_proxy.scheme + "://"]
        elif self.scheme:
            schemes = [self.scheme + "://"]
        else:
            schemes = ["http://", "https://", "socks5://", "socks4://"]

        status = None
        for scheme in schemes:
            try:
                if parsed_proxy.scheme:
                    formatted_proxy = proxy
                else:
                    formatted_proxy = scheme + proxy
                print(f"Scheme: {scheme}, Formatted proxy: {formatted_proxy}")

                proxies = {"http": formatted_proxy, "https": formatted_proxy}
                response = requests.get("http://google.com", proxies=proxies, timeout=5)
                status = response.status_code
                if status == 200:
                    print(f"Proxy {proxy} is good with {scheme[:-3]} scheme.")
                else:
                    print(
                        f"Proxy {proxy} failed with status code {status} for {scheme[-3]} scheme."
                    )
            except (
                requests.exceptions.RequestException,
                requests.exceptions.ConnectTimeout,
                requests.exceptions.ReadTimeout,
            ):
                print(f"Proxy {proxy} failed for {scheme[:-3]} scheme.")
                continue

        self.counter.increment()
        print(f"Checked {self.counter.value()} out of {self.total_proxies}")

        return proxy if status == 200 else None

    def filter_proxies(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
            return list(filter(None, executor.map(self.check_proxy, self.proxies)))
