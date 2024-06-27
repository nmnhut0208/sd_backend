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

# type Service = {
#     name: string;
#     code: string;
#     description?: string;
#     type: string; // [txt2img, img2img]
#     items: Array<ServiceItem>;
#     otherInfo?: Record<string, any>;
#   };

# type ServiceItem = {
#     name: string;
#     code: string;
#     properties: Array<ServiceItemProperty>;
#     description?: string;
#     imgUrl?: string;
#     payload?: Record<string, any>;
#     otherInfo?: Record<string, any>;
#   };

# type ServiceItemProperty = {
#     name: string;
#     type: string; // [input, select]
#     selectOptions?: Array<string>;
#   };

list_items = [
    {
        "name": "Text to Image",
        "code": "123",
        "type": "txt2img",
        "items": [
            {
                "name": "Sweety",
                "code": "sweety",
                "properties": [
                    {
                        "name": "style",
                        "type": "select",
                        "selectOptions": ["Sweety", "Realistic"]
                    },
                    {
                        "name": "img_url",
                        "type": "input"
                    }
                ],
                "description": "This is a description for Sweety style",
                "imgUrl": "https://example.com/sweety.jpg",
                "payload": {
                    "key1": "value1",
                    "key2": "value2"
                },
                "otherInfo": {
                    "key1": "value1",
                    "key2": "value2"
                }
            },
            {
                "name": "Realistic",
                "code": "realistic",
                "properties": [
                    {
                        "name": "style",
                        "type": "select",
                        "selectOptions": ["Sweety", "Realistic"]
                    },
                    {
                        "name": "img_url",
                        "type": "input"
                    }
                ],
                "description": "This is a description for Realistic style",
                "imgUrl": "https://example.com/realistic.jpg",
                "payload": {
                    "key1": "value1",
                    "key2": "value2"
                },
                "otherInfo": {
                    "key1": "value1",
                    "key2": "value2"
                }
            }
        ],
        "description": "This is a description for Text to Image service",
        "otherInfo": {
            "key1": "value1",
            "key2": "value2"
        }
    },
    {
        "name": "Image to Image",
        "code": "456",
        "type": "img2img",
        "items": [
            {
                "name": "Sweety",
                "code": "sweety",
                "properties": [
                    {
                        "name": "style",
                        "type": "select",
                        "selectOptions": ["Sweety", "Realistic"]
                    },
                    {
                        "name": "img_url",
                        "type": "input"
                    }
                ],
                "description": "This is a description for Sweety style",
                "imgUrl": "https://example.com/sweety.jpg",
                "payload": {
                    "key1": "value1",
                    "key2": "value2"
                },
                "otherInfo": {
                    "key1": "value1",
                    "key2": "value2"
                }
            },
            {
                "name": "Realistic",
                "code": "realistic",
                "properties": [
                    {
                        "name": "style",
                        "type": "select",
                        "selectOptions": ["Sweety", "Realistic"]
                    },
                    {
                        "name": "img_url",
                        "type": "input"
                    }
                ],
                "description": "This is a description for Realistic style",
                "imgUrl": "https://example.com/realistic.jpg",
                "payload": {
                    "key1": "value1",
                    "key2": "value2"
                },
                "otherInfo": {
                    "key1": "value1",
                    "key2": "value2"
                }
            }
        ],
        "description": "This is a description for Image to Image service",
        "otherInfo": {
            "key1": "value1",
            "key2": "value2"
        }
    }
]

api_url = "http://localhost:8111/backend/crud/create/cms"

for item in list_items:
    response = requests.post(api_url, json=item)
    print(response.json())