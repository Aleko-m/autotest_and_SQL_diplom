# Александр Малышев, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import data
import requests

# Функция создания заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # Подставляется URL и ручки
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

# Вызывается функция, передается тело запроса с данными
response = post_new_order(data.order_body);

# В переменную get_track сохраняется значение трек-номера, преобразованного из int в str
get_track = str(response.json()["track"])
print(response.json()["track"])

