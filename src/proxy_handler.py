import aiohttp
import asyncio
from src.proxy_checker import ProxyChecker
from src.file_handler import FileHandler


class ProxyHandler:

    @staticmethod
    def handle_proxies(full_input_path, proxies):
        if not proxies:
            proxies = FileHandler.read_from_file(full_input_path)

        checker = ProxyChecker(proxies)
        good_proxies = checker.filter_proxies()

        return good_proxies

    @staticmethod
    async def fetch_proxies_from_url(session, url):
        async with session.get(url) as response:
            text = await response.text()
            return text.splitlines()
        
    @staticmethod
    async def fetch_proxies_from_urls(urls):
        async with aiohttp.ClientSession() as session:
            return sum(
                await asyncio.gather(
                    *[ProxyHandler.fetch_proxies_from_url(session, url) for url in urls]
                ),
                [],
            )
    
    @staticmethod 
    def fetch_proxies(url):
        return asyncio.run(ProxyHandler.fetch_proxies_from_urls(url))

