import requests

def call_api():
    try:
        response = requests.get("https://api.example.com/data",
                                params={"key": "value"},
                                headers = {"Authorization": "Bearer YOUR_TOKEN"},
                                timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None