import json
import random
import string

import requests

from data_preparation.data_preparation_base import DataPreparationBase


class DataPreparationUser(DataPreparationBase):
    def create_user(self, random_data=True):
        url = DataPreparationBase.PETSTORE_BASE_URL + "user"
        payload = {}
        if random_data:
            payload = json.dumps({
                "id": get_random_id(),
                "username": get_random_username(),
                "firstName": get_random_name(),
                "lastName": get_random_name(),
                "email": get_random_email(),
                "password": "Yurec1989",
                "phone": get_random_phone_number(),
                "userStatus": 0,
            })
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
        }
        response = requests.post(
            url=url,
            data=payload,
            headers=headers,
        )
        return response, payload


def get_random_id():
    return random.randint(100000, 999999)


def get_random_username():
    length = 5
    chars = string.ascii_lowercase
    return "autotest" + "".join(random.choice(chars) for _ in range(length))


def get_random_name():
    length = 7
    chars = string.ascii_lowercase
    return "".join(random.choice(chars) for _ in range(length))


def get_random_email():
    domain = "gmail.com"
    length = 5
    chars = string.ascii_lowercase
    random_part = "".join(random.choice(chars) for _ in range(length))
    full_email = "qwerty123+" + random_part + "@" + domain
    return full_email


def get_random_phone_number():
    phone_random_number = [random.randint(0, 9) for _ in range(0, 7)]
    country = "380"
    operator = "67"
    full_random_phone_number = (
        country
        + operator
        + "".join(str(number) for number in phone_random_number)
    )
    return full_random_phone_number
