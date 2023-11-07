import requests

url = f"https://restcountries.com/v3.1/all"  # REST API
resp = requests.get(url)
countries = resp.json()

for country in sorted(countries, key=lambda c: c['area'])[-1:-11:-1]:
    name = country['name']['common']
    area = country['area']
    print(f"{name:50}  {area:10}")
