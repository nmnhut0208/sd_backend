import requests

url = 'http://localhost:8111/backend/makeup'

payload = {
    "style": "Sweety"
}


response = requests.post(url, json=payload)

print(response.json())