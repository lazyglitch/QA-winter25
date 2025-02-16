import pytest
from item_api import ItemAPI
import SHEMAS
from t_data import (
    test1_valid_data,
    test2_invalid_type_data,
    test4_negative_values_data,
    test5_missing_fields_data,
    test6_big_int_data,
)


# 1 создание объявления с корректными данными
@pytest.mark.parametrize("payload", test1_valid_data)
def test_create_item_with_valid_data(item_api, payload):
    response = item_api.create_item(payload)
    item_api.validate_response(response, 200, SHEMAS.CREATE_ITEM_SUCCESS_SCHEMA)


# 2 передача некорректныого типа данных
@pytest.mark.parametrize("field, value", test2_invalid_type_data)
def test_create_item_with_invalid_data_type(item_api, create_payload, field, value):
    payload = create_payload(field, value)
    response = item_api.create_item(payload)
    item_api.validate_response(response, 400, SHEMAS.ERROR_SCHEMA)


# 3 пустое тело запроса
@pytest.mark.xfail(reason="Bug ID 1")
def test_create_item_with_empty_body(item_api):
    response = item_api.create_item({})
    item_api.validate_response(response, 400, SHEMAS.ERROR_SCHEMA)


# 4 отрицательные значения
@pytest.mark.xfail(reason="Bug ID 2")
@pytest.mark.parametrize("field, value", test4_negative_values_data)
def test_create_item_with_negative_values(item_api, create_payload, field, value):
    payload = create_payload(field, value)
    response = item_api.create_item(payload)
    item_api.validate_response(response, 400, SHEMAS.ERROR_SCHEMA)


# 5 отсутствие обязательных полей
@pytest.mark.xfail(reason="Bug ID 3")
@pytest.mark.parametrize("missing_field", test5_missing_fields_data)
def test_create_item_with_missing_required_fields(
    item_api, create_payload, missing_field
):
    payload = create_payload()
    del payload[field]
    response = item_api.create_item(payload)
    item_api.validate_response(response, 400, SHEMAS.ERROR_SCHEMA)


# 6 длинный sellerID
@pytest.mark.parametrize("field, value", test6_big_int_data)
def test_create_item_with_big_int(item_api, create_payload, field, value):
    payload = create_payload(field, value)
    response = item_api.create_item(payload)
    item_api.validate_response(response, 400, SHEMAS.ERROR_SCHEMA)
