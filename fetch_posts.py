import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code == 200:
    posts = response.json()
    
    for i, post in enumerate(posts[:3]):
        print(f"{i+1}. {post['title']}")
    else:
        print("failed to retrieve posts:", response.status_code)