import requests
url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat"}
)

data = response.json()  # returns a dictionary
jokes = data["results"]
# print(data)
# print(data["results"])
# print(data["joke"])

for joke in jokes:
    print(joke["joke"])
    print("-----------")
