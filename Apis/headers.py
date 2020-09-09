import requests
url = "https://icanhazdadjoke.com/"

# response = requests.get(url, headers={"Accept": "text/plain"})

# request the data in json format
response = requests.get(url, headers={"Accept": "application/json"})

# print(response.text)
data = response.json()  # returns a dictionary

print(data)
print(data["joke"])
