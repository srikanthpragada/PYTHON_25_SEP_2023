import requests

code = input("Enter country code :")
url = f"https://restcountries.com/v3.1/alpha/{code}"  # REST API
resp = requests.get(url)
if resp.status_code == 404:
    print("Sorry! Country code not found!")
    exit(1)

country = resp.json()[0]

currencies = country['currencies']
cur_names = []
for c in currencies.keys():
    cur_names.append(currencies[c]['name'])

if 'capital' in country:
    capital = ','.join(country['capital'])
else:
    capital = 'No Capital'

print(f"Name       : {country['name']['common']}")
print(f"Capital    : {capital}")
print(f"Region     : {country['region']}")
print(f"Population : {country['population']}")
print(f"Area       : {country['area']}")
print(f"Currencies : {','.join(cur_names)}")

if 'borders' in country:
    borders = ','.join(country['borders'])
else:
    borders = 'No borders'

print(f"Borders    : {borders}")
