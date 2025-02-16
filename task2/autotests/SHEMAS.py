CREATE_ITEM_SUCCESS_SCHEMA = {
    "type": "object",
    "properties": {"status": {"type": "string"}},
    "required": ["status"],
}


ITEM_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "sellerId": {"type": "integer"},
            "name": {"type": "string"},
            "price": {"type": "integer"},
            "createdAt": {"type": "string"},
            "statistics": {
                "type": ["object", "null"],
                "properties": {
                    "likes": {"type": "integer"},
                    "viewCount": {"type": "integer"},
                    "contacts": {"type": "integer"},
                },
                "required": ["likes", "viewCount", "contacts"],
            },
        },
        "required": ["id", "sellerId", "name", "price", "statistics"],
    },
}

ERROR_SCHEMA = {
    "type": "object",
    "properties": {
        "result": {
            "type": "object",
            "properties": {
                "message": {"type": "string"},
                "messages": {"type": ["object", "null"]},
            },
            "required": ["message"],
        },
        "status": {"type": "string"},
    },
    "required": ["result", "status"],
}

STATISTICS_SCHEMA = {
    "type": "array",
    "items": {
        "type": ["object"],
        "properties": {
            "likes": {"type": "integer"},
            "viewCount": {"type": "integer"},
            "contacts": {"type": "integer"},
        },
        "required": ["likes", "viewCount", "contacts"],
    },
}
