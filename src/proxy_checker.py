import requests
import concurrent.futures
import logging
from urllib.parse import urlparse
from .counter import Counter
from .progress_bar import ProgressBar


DEFAULT_SCHEMES = ["http://", "https://", "socks5://", "socks4://"]
TARGET_URL = "http://google.com"
REQUEST_TIMEOUT = 5
MAX_WORKERS = 1000


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
            return DEFAULT_SCHEMES

    def format_proxy(self, scheme, proxy, parsed_proxy):
        return proxy if parsed_proxy.scheme else scheme + proxy

    def get_response(self, formatted_proxy):
        proxies = {"http": formatted_proxy, "https": formatted_proxy}
        try:
            return requests.get(TARGET_URL, proxies=proxies, timeout=REQUEST_TIMEOUT)
        except (
            requests.exceptions.RequestException,
            requests.exceptions.ConnectTimeout,
            requests.exceptions.ReadTimeout,
            requests.exceptions.SSLError,
            ValueError,
        ):
            return None

    def check_proxy(self, proxy):
        parsed_proxy = urlparse(proxy)
        schemes = self.get_schemes(parsed_proxy)

        for scheme in schemes:
            formatted_proxy = self.format_proxy(scheme, proxy, parsed_proxy)
            response = self.get_response(formatted_proxy)

            if response is not None and response.status_code == 200:
                self.counter.increment("Succeeded")
                return proxy

        else:
            self.counter.increment("Failed")
            return None

    def process_future(self, future, future_to_proxy, working_proxies):
        proxy = future_to_proxy[future]
        try:
            data = future.result()
        except Exception as exc:
            self.handle_exception(proxy, exc)
        else:
            if data is not None:
                working_proxies.append(data)
            else:
                if data is not None:
                    working_proxies.append(data)
        finally:
            self.counter.increment("Checked")

    def update_progress_bar(self, pbar):
        pbar.set_postfix(self.counter.values(), refresh=True)
        pbar.update(1)

    def filter_proxies(self):
        requests.packages.urllib3.disable_warnings()
        pbar = ProgressBar(self.total_proxies)

        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future_to_proxy = {
                executor.submit(self.check_proxy, proxy): proxy
                for proxy in self.proxies
            }

            for future in concurrent.futures.as_completed(future_to_proxy):
                proxy = future_to_proxy[future]
                try:
                    if future.result():
                        self.counter.increment("Succeeded")
                        pbar.update("Succeeded")
                    else:
                        self.counter.increment("Failed")
                        pbar.update("Failed")

                except Exception as exc:
                    self.handle_exception(proxy, exc)
                    self.counter.increment("Failed")
                    pbar.update("Failed")
                finally:
                    pbar.update("Checked")

        pbar.close()
        working_proxies = [
            proxy for future, proxy in future_to_proxy.items() if future.result()
        ]
        return working_proxies

    @classmethod
    def handle_exception(cls, proxy, exc):
        if not error_logger.hasHandlers():
            error_file_handler = logging.FileHandler("error.log")
            error_formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )
            error_file_handler.setFormatter(error_formatter)
            error_logger.addHandler(error_file_handler)
        error_logger.error("%r generated an exception: %s" % (proxy, exc))
