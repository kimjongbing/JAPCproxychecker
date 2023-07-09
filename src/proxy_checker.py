import requests
import concurrent.futures
import logging
from urllib.parse import urlparse
from .counter import Counter
from colorama import Fore, Style
from tqdm import tqdm

error_logger = logging.getLogger("error_logger")
error_logger.setLevel(logging.ERROR)


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
            requests.exceptions.SSLError,
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
                status = 200

        if status == 200:
            self.counter["Succeeded"] += 1
        else:
            self.counter["Failed"] += 1

        return proxy if status == 200 else None

    def filter_proxies(self):
        requests.packages.urllib3.disable_warnings()
        working_proxies = []
        self.counter = {"Checked": 0, "Succeeded": 0, "Failed": 0}
        with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
            future_to_proxy = {
                executor.submit(self.check_proxy, proxy): proxy
                for proxy in self.proxies
            }

            with tqdm(
                total=self.total_proxies, bar_format="{l_bar}{bar}| {postfix}"
            ) as pbar:
                pbar.set_postfix(self.counter, refresh=True)
                for future in concurrent.futures.as_completed(future_to_proxy):
                    proxy = future_to_proxy[future]
                    try:
                        data = future.result()
                    except Exception as exc:
                        if not error_logger.hasHandlers():
                            error_file_handler = logging.FileHandler("error.log")
                            error_formatter = logging.Formatter(
                                "%(asctime)s - %(levelname)s - %(message)s"
                            )
                            error_file_handler.setFormatter(error_formatter)
                            error_logger.addHandler(error_file_handler)
                        error_logger.error(
                            "%r generated an exception: %s" % (proxy, exc)
                        )
                        self.counter["Failed"] += 1
                    else:
                        if data is not None:
                            working_proxies.append(data)
                            self.counter["Succeeded"] += 1
                        else:
                            self.counter["Failed"] += 1
                    self.counter["Checked"] += 1
                    pbar.set_postfix(self.counter, refresh=True)
                    pbar.update(1)
        return working_proxies
