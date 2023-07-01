import concurrent.futures
import requests
import threading


class Counter:
    def __init__(self):
        self.val = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self.val += 1

    def value(self):
        with self._lock:
            return self.val

def check_proxy(proxy):
    print(f"Checking proxy: {proxy}")
    try:
        response = requests.get('http://google.com', proxies={'http': proxy, 'https': proxy}, timeout=5)
        if response.status_code == 200:
            print(f"Proxy {proxy} is good.")
            counter.increment()  # increment the counter
            print(f"Checked {counter.value()} out of {total_proxies}")
            return proxy
        else:
            print(f"Proxy {proxy} failed with status code {response.status_code}.")
            counter.increment()  # increment the counter
            print(f"Checked {counter.value()} out of {total_proxies}")
            return None
    except (requests.exceptions.RequestException, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
        print(f"Proxy {proxy} failed.")
        counter.increment()  # increment the counter
        print(f"Checked {counter.value()} out of {total_proxies}")
        return None


def main():
    global counter
    global total_proxies


    with open('http.txt', 'r') as f:
        proxies = [line.strip() for line in f.readlines()]

    total_proxies = len(proxies)
    counter = Counter()


    with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
        good_proxies = list(filter(None, executor.map(check_proxy, proxies)))

   
    with open('http.txt', 'w') as f:
        for proxy in good_proxies:
            f.write(f"{proxy}\n")
    
if __name__ == '__main__':
    main()

#automatically grab these
# these proxies worked well, good to use for testing unless it was a fluke lol. https://github.com/mertguvencli/http-proxy-list/blob/main/proxy-list/data.txt