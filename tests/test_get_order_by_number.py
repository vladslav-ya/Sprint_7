import requests
import data
import json
import pytest


class TestGetOrderByNumber:

    def test_get_order_by_number_positive_check_response(self):
        payload = json.dumps(data.ORDER_DATA)
        order_response = requests.post(f'{data.TEST_URL}/api/v1/orders', data=payload)
        track_number = order_response.json().get("track")

        response = requests.get(f'{data.TEST_URL}/api/v1/orders/track', params={"t": track_number})

        assert response.status_code == 200, "Response code is not 200"
        assert response.json().get("order"), "Field 'order' missing or empty"

    @pytest.mark.parametrize("negative_data", data.NEGATIVE_ORDER_TRACKS)
    def test_get_order_by_number_negative_check_response(self, negative_data):
        track_number, code, message = negative_data

        response = requests.get(f'{data.TEST_URL}/api/v1/orders/track', params={"t": track_number})

        assert response.status_code == code, f"Response code is not {code}"
        assert response.json()["message"] == message, "Wrong message"