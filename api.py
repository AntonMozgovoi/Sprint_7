import requests
from urls import Urls


class CourierApi:
    @staticmethod
    def creation_courier(body):
        req_body = requests.post(Urls.BASE_URL + Urls.REGISTRATION_COURIER, json=body)
        return req_body





