from bs4 import BeautifulSoup
import requests

try:
    resp = requests.get("https://www.tiobe.com/tiobe-index")
    contents = resp.text

    bs = BeautifulSoup(contents, 'html.parser')

    top20_table = bs.find(id="top20")
    body = top20_table.find("tbody")

    for row in body.find_all("tr")[:10]:
        cols = row.find_all("td")
        print(f"{cols[4].text:20}  - {cols[5].text}")

except Exception as ex:
    print("Sorry! Could not get details. Error --> " + ex)




