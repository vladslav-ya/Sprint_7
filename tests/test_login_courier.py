import requests
import data


class TestLoginCourier:

    def test_login_courier_positive_check_response(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password

        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(f'{data.TEST_URL}/api/v1/courier/login', data=payload)

        assert response.status_code == 200, "Response code is not 200"
        assert response.json().get("id"), "Field 'id' missing or empty"

    def test_login_courier_without_login_check_response(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password

        payload = {
            "password": password
        }

        response = requests.post(f'{data.TEST_URL}/api/v1/courier/login', data=payload)

        assert response.status_code == 400, "Response code is not 400"
        assert response.json()["message"] == "Недостаточно данных для входа", "Wrong response body"

    def test_wrong_credentials_check_response(self):
        login, password = data.WRONG_CREDENTIALS

        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(f'{data.TEST_URL}/api/v1/courier/login', data=payload)

        assert response.status_code == 404, "Response code is not 404"
        assert response.json()["message"] == "Учетная запись не найдена", "Wrong response body"
