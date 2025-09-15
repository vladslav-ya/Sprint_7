import requests
import random
import string
import pytest
import data
import json


@pytest.fixture(scope="class")
def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f'{data.TEST_URL}/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


@pytest.fixture(scope="class")
def register_new_courier_and_return_id(register_new_courier_and_return_login_password):
    courier_id = None
    login, password, _ = register_new_courier_and_return_login_password
    payload = {"login": login, "password": password}

    response = requests.post(f'{data.TEST_URL}/api/v1/courier/login', data=payload)

    if response.status_code == 200:
        courier_id = response.json().get("id")

    yield courier_id
    if courier_id is not None:
        delete_response = requests.delete(f'{data.TEST_URL}/api/v1/courier/{courier_id}')
        assert delete_response.status_code == 200


@pytest.fixture(scope="class")
def create_new_order_and_return_id():
    order_id = None
    payload = json.dumps(data.ORDER_DATA)
    order_response = requests.post(f'{data.TEST_URL}/api/v1/orders', data=payload)
    track_number = order_response.json().get("track")

    response = requests.get(f'{data.TEST_URL}/api/v1/orders/track', params={"t": track_number})

    if response.status_code == 200:
        order_id = response.json().get("order")["id"]
    yield order_id
    if order_id is not None:
        finish_response = requests.put(f'{data.TEST_URL}/api/v1/orders/finish/{order_id}')
        assert finish_response.status_code == 200
