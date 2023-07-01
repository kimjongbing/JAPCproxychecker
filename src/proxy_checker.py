import requests
import concurrent.futures
from .counter import Counter

class ProxyChecker:
    def __init__(self, proxies):
        self.proxies = proxies
        self.total_proxies = len(proxies)
        self.counter = Counter()

    def check_proxy(self, proxy):
        print(f"Checking proxy: {proxy}")
        status = None
        try:
            response = requests.get('http://google.com', proxies={'http': proxy, 'https': proxy}, timeout=5)
            status = response.status_code
            if status == 200:
                print(f"Proxy {proxy} is good.")
            else:
                print(f"Proxy {proxy} failed with status code {status}.")
        except (requests.exceptions.RequestException, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
            print(f"Proxy {proxy} failed.")

        self.counter.increment() 
        print(f"Checked {self.counter.value()} out of {self.total_proxies}")

        return proxy if status == 200 else None

    def filter_proxies(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
            return list(filter(None, executor.map(self.check_proxy, self.proxies)))
