from faker import Faker
from data import TestRegistration


class TestDataHelper:
    @staticmethod
    def modify_registration_body_request(key, value):
        body = TestRegistration.REGISTRATION_COURIER_BODY.copy()
        body[key] = value
        return body

    @staticmethod
    def generate_registration_body():
        fake = Faker()
        return TestDataHelper.modify_registration_body_request('login', fake.name())

