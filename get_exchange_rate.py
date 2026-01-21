import requests

API_KEY = "ed9315d06ac8894b548723ae"
base_url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

try:
    response = requests.get(base_url, timeout=10)
    response.raise_for_status()  # Raise an error for bad status codes
    data = response.json()

    if data.get("result") == "success":
        cny_rate = data["conversion_rates"]["CNY"]
        print(f"1 USD is equal to {cny_rate} CNY")
    else:
        print("API returned an error:", data.get("error-type", "Unknown error"))
    
except requests.exceptions.RequestException as e:
    print("An error occurred while fetching the exchange rate:", e)
except KeyError:
    print("Could not find the CNY exchange rate in the response.")