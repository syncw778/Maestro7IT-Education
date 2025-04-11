import json

address_info = {
    "country": "rus",
    "city": "moscow",
    "zip_code": "99608",
    "floor": "10",
    "has_intercom": True
}

print(json.dumps(address_info, indent=4))