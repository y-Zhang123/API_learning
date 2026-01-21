import requests

params = {"userId": 1}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)

if response.status_code == 200:
    posts = response.json()
    print(f"found {len(posts)} posts for userId=1")
    for p in posts[:2]:
        print(f"- {p['title']}")

# what does this code do? 
# This code retrieves all posts for a specific user (userId=1) from a REST API endpoint and prints the titles of the first two posts.
# what if there is no posts for userId=1?
# If there are no posts for userId=1, the code will print "found 0 posts for userId=1" and will not print any post titles.