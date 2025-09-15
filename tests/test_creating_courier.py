import requests
import random
import string
import data
import allure


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


class TestCreatingCourier:

    @allure.title('Проверка позитивного сценария создания курьера')
    @allure.description('Все обязательные поля заполнены при создании')
    def test_register_new_courier_positive_check_response(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(f'{data.TEST_URL}/api/v1/courier', data=payload)

        assert response.status_code == 201, "Response code is not 201"
        assert response.json() == {"ok": True}, "Wrong response body"

    @allure.title('Проверка создание одинаковых курьеров')
    @allure.description('Создание курьера, после создание курьера с теми же данными')
    def test_cant_create_similar_new_courier_check_response(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        requests.post(f'{data.TEST_URL}/api/v1/courier', data=payload)

        response_negative = requests.post(f'{data.TEST_URL}/api/v1/courier', data=payload)
        assert response_negative.status_code == 409, "Response code is not 409"
        assert response_negative.json()["message"] == "Этот логин уже используется. Попробуйте другой.", "Wrong response body"

    @allure.title('Проверка создание курьера без обязательного поля password')
    @allure.description('Негативный сценарий без поля password')
    def test_cant_create_new_courier_without_required_field_check_response(self):
        login = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "firstName": first_name
        }

        response_negative = requests.post(f'{data.TEST_URL}/api/v1/courier', data=payload)
        assert response_negative.status_code == 400, "Response code is not 400"
        assert response_negative.json()["message"] == "Недостаточно данных для создания учетной записи", "Wrong response body"
