import json
import requests

# url_data = "assets/data.json"
# data = json.load(open(url_data))

### convert to struct {"category": "MakeUp", "subcategory": "Realistic", "style": "Sweety", "img_url": "https://example.com/sweety.jpg", "payload": {...}}
# list_items = []

# for category, items_subcategory in data.items():
#     for subcategory, items_style in items_subcategory.items():
#         for item in items_style:
#             list_items.append({"category": category, "subcategory": subcategory, "style": item["style"], "img_url": item["img_url"], "payload": item["payload"]})

list_items = [
    {
        "id": "123",
        "name": "MakeUp",
        "code": "123",
        "type": "123",
        "description": "test description",
    }
]

api_url = "http://localhost:8111/backend/crud/create/cms"

for item in list_items:
    response = requests.post(api_url, json=item)
    print(response.json())