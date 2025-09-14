import requests
import data
import pytest


class TestAcceptOrder:

    def test_accept_order_positive_check_response(self, register_new_courier_and_return_id, create_new_order_and_return_id):
        order_id = create_new_order_and_return_id
        courier_id = register_new_courier_and_return_id

        response = requests.put(f'{data.TEST_URL}/api/v1/orders/accept/{order_id}', params={"courierId": courier_id})

        print(response.json())


        assert response.status_code == 200, "Response code is not 200"
        assert response.json() == {"ok": True}, "Wrong response body"

    @pytest.mark.parametrize("negative_data", data.NEGATIVE_ORDER_DATA)
    def test_wrong_ids_negative_check_response(self, register_new_courier_and_return_id, create_new_order_and_return_id, negative_data):
        if type(negative_data["order_id"]) == int:
            order_id = negative_data["order_id"]
        elif negative_data["order_id"] is False:
            order_id = ""
        else:
            order_id = create_new_order_and_return_id

        if type(negative_data["courier_id"]) == int:
            courier_id = negative_data["courier_id"]
        elif negative_data["courier_id"] is False:
            courier_id = ""
        else:
            courier_id = register_new_courier_and_return_id

        response = requests.put(f'{data.TEST_URL}/api/v1/orders/accept/{order_id}', params={"courierId": courier_id})

        print(response.json())

        assert response.status_code == negative_data["code"], f"Response code is not {negative_data["code"]}"
        assert response.json()["message"] == negative_data["message"], "Wrong response body"
