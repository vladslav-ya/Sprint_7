import pytest
import requests
import data
import json


class TestCreatingOrder:

    @pytest.mark.parametrize("color", data.COLOR_VARIANTS)
    def test_creating_order_positive_check_response(self, color):
        prep_payload = data.ORDER_DATA
        prep_payload["color"] = color
        payload = json.dumps(prep_payload)

        response = requests.post(f'{data.TEST_URL}/api/v1/orders', data=payload)

        assert response.status_code == 201, "Response code is not 201"
        assert response.json().get("track"), "Field 'track' missing or empty"
