import requests

url = f"https://restcountries.com/v3.1/all"  # REST API
resp = requests.get(url)
countries = resp.json()

for country in countries:
    name = country['name']['common']
    if 'capital' in country:
        capital = country['capital'][0]
    else:
        capital = 'Unknown'

    population = country['population']

    print(f"{name:50}  {capital:30} {population:10}")
