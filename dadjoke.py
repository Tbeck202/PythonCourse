import requests
import random
url = "https://icanhazdadjoke.com/search"

topic = input("Let me tell you a joke! Give me a topic: ")

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": topic}
)

data = response.json()
jokes = []
if len(data["results"]) < 1:
    print(f"Sorry, I don;t have any jokes about {topic}")
else:
    for item in data["results"]:
        jokes.append(item)

if len(jokes) == 1:
    # joke = jokes[0]['joke']
    print(f"I have one joke about {topic}: {jokes[0]['joke']}")
elif len(jokes) > 1:
    num = len(jokes)
    random = random.randint(0, num)
    print(f"I have {num} jokes about {topic}! Here's one of them:")
    print(jokes[random]["joke"])
