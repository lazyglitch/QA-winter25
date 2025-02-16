import pytest
from item_api import ItemAPI

BASE_URL = "https://qa-internship.avito.com/api/1"


@pytest.fixture
def item_api():
    return ItemAPI(BASE_URL)


@pytest.fixture
def create_payload():

    def _create_payload(field=None, value=None):
        payload = {
            "sellerID": 1234345271,
            "name": "new post",
            "price": 1,
            "statistics": {},
        }
        if field:
            if field in payload:
                payload[field] = value
            else:
                payload["statistics"][field] = value
        return payload

    return _create_payload
