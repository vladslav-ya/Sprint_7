import requests
import data


class TestGetListOrders:

    def test_get_list_orders_positive_check_response(self):
        response = requests.get(f'{data.TEST_URL}/api/v1/orders')

        assert response.status_code == 200, "Response code is not 200"
        assert response.json().get("orders"), "Field 'orders' missing or empty"
