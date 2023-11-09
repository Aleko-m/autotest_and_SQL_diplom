# Александр Малышев, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import create_orders_request

# Функция получения заказа по трек-номеру
def get_order_track():
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_TRACK_PATH + create_orders_request.get_track) # Подставляется URL и ручки
response = get_order_track() # В переменную response записывается результат выполнения функции

# Функция проверки, что код ответа равен 200
def test_get_order_track():
    # Проверяется, что код ответа равен 200
    assert response.status_code == 200, "Тест не пройден: код ответа не 200"
# Вызывается функция проверки, что код ответа равен 200
test_get_order_track()

