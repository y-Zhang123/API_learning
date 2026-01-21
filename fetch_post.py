import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

if response.status_code == 200:
    data = response.json()
    print("title:", data["title"])
    print("body:", data["body"])
else:
    print("Failed to retrieve data:", response.status_code)