#Simple example to understand multiprocessing

import requests
from bs4 import BeautifulSoup
import time
import multiprocessing

#List of URLs to retrieve
urls =["https://google.com","https://example.com","https://portswigger.net","https://owasp.org","https://twitter.com","https://github.com","https://youtube.com","https://instagram.com","https://shopify.com","https://starbucks.com","https://python.org"]

#Function to retrieve URLs and the webpage title
def getUrl(url):
  resp = requests.get(url)
  return (str(BeautifulSoup(resp.text,"html.parser").find("title")))

#Single Threaded version
s = time.perf_counter()
print([getUrl(u) for u in urls])
elapsed = time.perf_counter() - s
print(f"{elapsed:0.2f} seconds")

#Five threads version
s = time.perf_counter()
p = multiprocessing.Pool(5)
data = p.map(getUrl,[url for url in urls])
p.close()
print(data)
elapsed = time.perf_counter() - s
print(f"{elapsed:0.2f} seconds")

# Ten threads version
s = time.perf_counter()
p = multiprocessing.Pool(10)
data = p.map(getUrl,[url for url in urls])
p.close()
print(data)
elapsed = time.perf_counter() - s
print(f"{elapsed:0.2f} seconds")