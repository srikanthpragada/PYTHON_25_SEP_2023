from bs4 import BeautifulSoup
import requests

resp = requests.get("http://www.srikanthtechnologies.com")
contents = resp.text

bs = BeautifulSoup(contents, 'html.parser')

batch_table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
rows = batch_table.find_all("tr")[1:]  # 0th row is headings

for row in rows:
    cols = row.find_all("td")
    print(cols[1].text)  # Course title
    print(f"{cols[3].text}  -  {cols[5].text}")  # Start date to End date
    print('-' * 30)





