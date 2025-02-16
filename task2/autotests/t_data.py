# валидные данные
test1_valid_data = [
    {
        "sellerID": 1234345231,
        "name": "new post",
        "price": 1,
        "statistics": {"contacts": 0, "likes": 0, "viewCount": 0},
    }
]

# некорректные типы данных
test2_invalid_type_data = [
    ("sellerID", "1234345231"),
    ("name", 10),
    ("price", "1000"),
    ("contacts", "0"),
    ("likes", "0"),
    ("viewCount", "0"),
]

# отрицательные значения
test4_negative_values_data = [
    ("sellerID", -1234345231),
    ("price", -10),
    ("contacts", -5),
    ("likes", -10),
    ("viewCount", -10),
]

# отсутствие обязательных полей
test5_missing_fields_data = [["sellerID"], ["name"], ["price"]]

# большие числа
test6_big_int_data = [
    ("sellerID", 1234345231369696939995),
    ("price", 10000000000000000000),
    ("contacts", 55555555555555555555),
    ("likes", 55555555555555555555),
    ("viewCount", 55555555555555555555),
]
