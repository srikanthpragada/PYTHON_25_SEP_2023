from bs4 import BeautifulSoup
import requests

WEBSITE = "https://www.w3schools.com"
resp = requests.get(WEBSITE)
contents = resp.text


bs = BeautifulSoup(contents, 'html.parser')
urls = []
for a in bs.find_all("a"):
    href = a['href']
    if href.startswith("javascript"):
        continue

    if not href.startswith("http"):
        href= WEBSITE + href

    if href not in urls:
        urls.append(href)

for href in urls:
    print(href)







