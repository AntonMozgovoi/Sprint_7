import allure
import requests
from urls import Urls
from api import CourierApi
from data import TestRegistration
from helper import TestDataHelper


class TestRegistrationCourier:
    @allure.title('Проверка успешной регистрации курьера')
    @allure.description('Проверяем успешный статус и ok: true в теле ответа')
    def test_creation_new_courier(self):
        registration_request = CourierApi.creation_courier(TestDataHelper.generate_registration_body())
        assert registration_request.status_code == 201 and registration_request.json()["ok"] == True

    @allure.title('Проверка неуспешной повторной авторизации курьера с одинаковым логином')
    @allure.description('Проверяем статус 409 и сообщением "Этот логин уже используется. Попробуйте другой." в теле ответа')
    def test_creation_same_courier(self):  # Нельзя создать двух одинаковых курьеров, при создании курьера с одинаковым логином возвращается ошибка с текстом
        body = TestDataHelper.generate_registration_body()
        CourierApi.creation_courier(body)
        creation_request = CourierApi.creation_courier(body)
        assert creation_request.status_code == 409 and creation_request.json()["message"] == (
            "Этот логин уже используется. Попробуйте другой.")

    @allure.title('Проверка неуспешной повторной авторизации курьера без параметра')
    @allure.description('Проверяем статус 400 и сообщением "Недостаточно данных для создания учетной записи" в теле ответа')
    def test_wrong_body(self):
        wrong_body = TestRegistration.REGISTRATION_WRONG_BODY
        wrong_registration_request = requests.post(Urls.BASE_URL + Urls.REGISTRATION_COURIER, data=wrong_body)
        assert wrong_registration_request.status_code == 400 and wrong_registration_request.json()["message"] == (
            "Недостаточно данных для создания учетной записи")
