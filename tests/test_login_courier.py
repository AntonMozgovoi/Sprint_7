import allure
import requests
from urls import Urls
from data import TestLogin


class TestLoginCourier:
    @allure.title('Проверка успешной авторизации курьера')
    @allure.description('Проверяем успешный статус и id курьера в теле ответа')
    def test_login_courier(self):
        login_body = TestLogin.LOGIN_COURIER
        login_request = requests.post(Urls.BASE_URL + Urls.LOGIN_COURIER, data=login_body)
        assert login_request.status_code == 200 and login_request.json()["id"] == 213383

    @allure.title('Проверка неуспешной авторизации с неверным логином')
    @allure.description('Проверяем статус 404 и текст ошибки "Учетная запись не найдена" в теле ответа')
    def test_wrong_login(self):
        login_body = TestLogin.WRONG_LOGIN
        login_request = requests.post(Urls.BASE_URL + Urls.LOGIN_COURIER, data=login_body)
        assert login_request.status_code == 404 and login_request.json()["message"] == "Учетная запись не найдена"

    @allure.title('Проверка неуспешной авторизации курьера без одного параметра')
    @allure.description('Проверяем статус 400 и текст ошибки "Недостаточно данных для входа"')
    def test_without_login(self):
        login_body = TestLogin.REQ_WITHOUT_LOGIN
        login_request = requests.post(Urls.BASE_URL + Urls.LOGIN_COURIER, data=login_body)
        assert login_request.status_code == 400 and login_request.json()["message"] == "Недостаточно данных для входа"



