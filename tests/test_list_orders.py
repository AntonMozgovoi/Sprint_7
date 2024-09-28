import allure
import requests
from urls import Urls


class TestLoginCourier:
    @allure.title('Проверка возврата списка заказов')
    @allure.description('Проверяем успешный ответ и наличие списка заказов')
    def test_login_courier(self):   # успешная авторизация курьера
        login_request = requests.get(Urls.BASE_URL + Urls.LIST_ORDERS)
        r = login_request.json()
        assert login_request.status_code == 200 and r["orders"][0]