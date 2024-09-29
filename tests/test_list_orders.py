import allure
import requests
from urls import Urls


class TestOrderList:
    @allure.title('Проверка возврата списка заказов')
    @allure.description('Проверяем успешный ответ и наличие списка заказов')
    def test_order_list(self):   # успешная авторизация курьера
        order_list = requests.get(Urls.BASE_URL + Urls.LIST_ORDERS)
        response = order_list.json()
        assert order_list.status_code == 200 and response["orders"][0]