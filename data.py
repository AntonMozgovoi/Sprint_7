class TestRegistration:
    REGISTRATION_COURIER_BODY = {
        "login": "ninja1",
        "password": "1234",
        "firstName": "saske"
    }

    REGISTRATION_WRONG_BODY = {
        "password": "1234",
        "firstName": "saske"
    }


class TestLogin:
    LOGIN_COURIER = {
        "login": "anton",
        "password": "1234"
    }

    WRONG_LOGIN = {
        "login": "wrong_login",
        "password": "1234"
    }

    REQ_WITHOUT_LOGIN = {
        "password": "1234"
    }


class TestOrder:
    ORDER = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }
