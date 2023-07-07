import aiohttp
import asyncio

async def fetch_proxies_from_url(session, url):
    async with session.get(url) as response:
        text = await response.text()
        return text.splitlines()

async def fetch_proxies_from_urls(urls):
    async with aiohttp.ClientSession() as session:
        return sum(await asyncio.gather(*[fetch_proxies_from_url(session, url) for url in urls]), [])

def fetch_proxies(url):
    return asyncio.run(fetch_proxies_from_urls(url))
