import pytest
from item_api import ItemAPI
import SHEMAS


# 13 получение статистики по существующему id
def test_get_statistics_valid(item_api, create_payload):
    payload = create_payload("sellerID", 12345)
    new_item = item_api.create_item(payload)
    item_id = item_api.get_created_item_id(new_item)
    response = item_api.get_statistics(item_id)
    item_api.validate_response(response, 200, SHEMAS.STATISTICS_SCHEMA)


# 14 получение статистики по некорректному id
def test_get_statistics_invalid_id(item_api):
    response = item_api.get_statistics("qwerty12345")
    item_api.validate_response(response, 400, SHEMAS.ERROR_SCHEMA)


# 15 получение статистики по несуществующему id
def test_get_statistics_nonexistent_id(item_api):
    non_existent_id = "0c84183f-a699-4486-83f8-b513dfde4777"
    response = item_api.get_statistics(non_existent_id)
    item_api.validate_response(response, 404, SHEMAS.ERROR_SCHEMA)
