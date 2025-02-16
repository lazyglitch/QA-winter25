import requests
from jsonschema import validate


class ItemAPI:

    def __init__(self, base_url):
        self.base_url = base_url

    def create_item(self, payload, endpoint="item"):
        response = requests.post(f"{self.base_url}/{endpoint}", json=payload)
        return response

    def get_created_item_id(self, response):
        return response.json()["status"].split()[-1]

    def get_item_by_id(self, ID, endpoint="item"):
        response = requests.get(f"{self.base_url}/{endpoint}/{ID}")
        return response

    def get_item_by_seller_id(self, ID, endpoint="item"):
        response = requests.get(f"{self.base_url}/{ID}/{endpoint}")
        return response

    def get_statistics(self, item_id, endpoint="statistic"):
        response = requests.get(f"{self.base_url}/{endpoint}/{item_id}")
        return response

    def validate_response(self, response, expected_status, schema):
        assert response.status_code == expected_status, "Неверный статус код"
        validate(instance=response.json(), schema=schema)
