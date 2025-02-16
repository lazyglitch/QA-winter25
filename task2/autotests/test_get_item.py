import pytest
from item_api import ItemAPI
import SHEMAS


# 7 получение объявления по существующему id
def test_get_item_by_valid_id(item_api, create_payload):
    payload = create_payload("sellerID", 55112)
    new_item = item_api.create_item(payload)
    item_id = item_api.get_created_item_id(new_item)
    response = item_api.get_item_by_id(item_id)
    item_api.validate_response(response, 200, SHEMAS.ITEM_SCHEMA)
    assert response.json()[0]["id"] == item_id


# 8 получение объявления по некорректному id
def test_get_item_by_invalid_id(item_api):
    response = item_api.get_item_by_id("qwerty12345")
    item_api.validate_response(response, 400, SHEMAS.ERROR_SCHEMA)


# 9 получение объявления по несуществующему id
def test_get_item_by_nonexistent_id(item_api):
    response = item_api.get_item_by_id("0cd4183f-a699-4486-83f8-b513dfde4777")
    item_api.validate_response(response, 404, SHEMAS.ERROR_SCHEMA)


# 10 получение объявления по валидному sellerID
def test_get_items_valid_sellerId(item_api, seller_id=551239):
    response = item_api.get_item_by_seller_id(seller_id)
    item_api.validate_response(response, 200, SHEMAS.ITEM_SCHEMA)
    items = response.json()
    assert all(item["sellerId"] == seller_id for item in items)


# ниже тест для проверки использует уникальное значение seller_id, поэтому его надо каждый раз менять вручную
# варианты незанятых seller_id: 551231 / 551251 / 551271 / 551273
""" @pytest.mark.skip  
# 10 получение объявления по валидному sellerID
def test_get_items_by_valid_sellerId(item_api, create_payload):
    seller_id = 551239  # надо заменить
    num = 2
    for _ in range(num):
        payload = create_payload("sellerID", seller_id)
        item_api.create_item(payload)

    response = item_api.get_item_by_seller_id(seller_id)
    item_api.validate_response(response, 200, SHEMAS.ITEM_SCHEMA)
    items = response.json()
    assert len(items) == num, "Неверное количество объявлений" """


# 11 получение объявления по некорректному sellerID
def test_get_items_invalid_seller_id(item_api):
    response = item_api.get_item_by_seller_id("qwerty12345")
    item_api.validate_response(response, 400, SHEMAS.ERROR_SCHEMA)


# 12 получение объявления по несуществующему sellerID
@pytest.mark.xfail(reason="Bug ID 4")
def test_get_item_by_nonexistent_sellerId(item_api):
    response = item_api.get_item_by_seller_id("99111")
    item_api.validate_response(response, 400, SHEMAS.ERROR_SCHEMA)
