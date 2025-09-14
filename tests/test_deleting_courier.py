import requests
import data
import pytest


class TestDeletingCourier:

    def test_deleting_courier_positive_check_response(self, register_new_courier_and_return_login_password):
        login, password, _ = register_new_courier_and_return_login_password
        payload = {"login": login, "password": password}
        response = requests.post(f'{data.TEST_URL}/api/v1/courier/login', data=payload)
        courier_id = response.json().get("id")

        response = requests.delete(f'{data.TEST_URL}/api/v1/courier/{courier_id}')

        assert response.status_code == 200, "Response code is not 200"
        assert response.json() == {"ok": True}, "Wrong response body"

        requests.delete(f'{data.TEST_URL}/api/v1/courier/{courier_id}')

    @pytest.mark.parametrize("courier_data", data.NEGATIVE_COURIER_DATA)
    def test_deleting_courier_negative_id_check_response(self, courier_data):
        c_id, code, message = courier_data

        response = requests.delete(f'{data.TEST_URL}/api/v1/courier/{c_id}')

        assert response.status_code == code, f"Response code is not {code}"
        assert response.json()["message"] == message, "Wrong response body"
