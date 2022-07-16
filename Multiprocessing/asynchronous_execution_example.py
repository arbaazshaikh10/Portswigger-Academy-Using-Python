#Simple example to understand asynchronous execution

import asyncio
import multiprocessing
import requests_async
from bs4 import BeautifulSoup
import time

#List of URLs to retrieve
urls =["https://google.com","https://example.com","https://portswigger.net","https://owasp.org","https://twitter.com","https://github.com","https://youtube.com","https://instagram.com","https://shopify.com","https://starbucks.com","https://python.org"]

async def agetUrl(url):
  resp = await requests_async.get(url)
  return (str(BeautifulSoup(resp.text,'html.parser').find('title')))

async def async_main(urls):
  tasks = [agetUrl(u) for u in urls]
  return (await asyncio.gather(*tasks))

s = time.perf_counter()
print(asyncio.run(async_main(urls)))
elapsed = time.perf_counter() - s
print(f'{elapsed:0.2f}')