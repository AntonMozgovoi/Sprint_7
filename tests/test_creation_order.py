import allure
import pytest
import requests
import data
from urls import Urls


class TestCreationOrder:
    @allure.title('Проверка создания заказа')
    @allure.description('Проверяем успешный ответ и содержание track с указанием цветов BLACK или GREY, двух цветов и без указания цвета ')
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], [], ["BLACK", "GREY"]])

    def test_creation_order_color(self, color):
        login_body = data.TestOrder.ORDER
        login_request = requests.post(Urls.BASE_URL + Urls.CREATION_ORDER, json=login_body)
        response = login_request.json()
        assert login_request.status_code == 201 and response["track"]