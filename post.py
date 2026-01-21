import requests

new_post = {
    "title": "New Post Title",
    "body": "This is the body of the new post.",
    "userId": 1
}  

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)

# response.status_code possible values:
# 201: Created successfully
# 400: Bad Request 
# 500: Internal Server Error
# 200: OK
if response.status_code == 201:
    created = response.json()
    print("Created successfully, ID:", created['id'])
else:
    print("Failed to create post:", response.status_code)