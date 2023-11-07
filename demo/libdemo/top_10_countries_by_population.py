import requests

url = f"https://restcountries.com/v3.1/all"  # REST API
resp = requests.get(url)
countries = resp.json()

for country in sorted(countries,
                       key=lambda c: c['population'])[-1:-11:-1]:
    name = country['name']['common']
    population = country['population']
    area = country['area']
    print(f"{name:50}  {population:10}   {area:10}")
