import requests
import data
import allure


class TestGetListOrders:

    @allure.title('Проверка получения списка заказов')
    @allure.description('Позитивный сценарий проверка получения списка заказов')
    def test_get_list_orders_positive_check_response(self):
        response = requests.get(f'{data.TEST_URL}/api/v1/orders')

        assert response.status_code == 200, "Response code is not 200"
        assert response.json().get("orders"), "Field 'orders' missing or empty"
