import json

with open("api_key.json", "r") as file:
    api_keys = json.load(file)

api_key = api_keys["api_key"]
api_secret = api_keys["api_secret"]

print(api_key)
print(api_secret)

