TEST_URL = "https://qa-scooter.praktikum-services.ru"

WRONG_CREDENTIALS = ["wrong_login", "wrong_pass"]

NEGATIVE_COURIER_DATA = [["", 400, "Недостаточно данных для удаления курьера"], [99999999, 404, "Курьера с таким id нет."]]

ORDER_DATA = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2025-12-28",
    "comment": "Saske, come back to Konoha",
    "color": []
}

COLOR_VARIANTS = [["BLACK"], ["GREY"], ["BLACK", "GREY"], []]

NEGATIVE_ORDER_DATA = [{"courier_id": False, "order_id": True, "code": 400, "message": "Недостаточно данных для поиска"},
                       {"courier_id": 99999999, "order_id": True, "code": 404, "message": "Курьера с таким id не существует"},
                       {"order_id": True, "courier_id": False, "code": 400, "message": "Недостаточно данных для поиска"},
                       {"courier_id": True, "order_id": 99999999, "code": 404, "message": "Заказа с таким id не существует"}
                       ]

NEGATIVE_ORDER_TRACKS = [["", 400, "Недостаточно данных для поиска"], [99999999, 404, "Заказ не найден"]]