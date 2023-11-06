import requests

username = input("Enter github username: ")
url = f"https://api.github.com/users/{username}"  # REST API
resp = requests.get(url)
if resp.status_code == 404:  # not found
    print(f"Sorry! Name - {username} - not found!")
    exit(1)

if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit(2)

details = resp.json()  # Convert response(JSON) to dict

print(details['name'])
print(details['company'])
print(details['location'])
print(details['created_at'])
