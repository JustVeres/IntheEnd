import for_request #подключаем for_request.py
import requests #подключаем библиотеку запросов
import body #подключаем body.py

def create_an_order(body): #функция для создания заказа
    return requests.post(for_request.URL + for_request.CREATE_AN_ORDER_API,
                         json=body.body_order)

response_create_an_order = create_an_order(body) #сохраняем номер трека заказа
#print(response_create_an_order.json()) #расскоментировать для проверки

def get_an_order_by_number(): #функция на получение заказа по треку
    return requests.get(for_request.URL + for_request.GET_AN_ORDER_BY_NUMBER_API,
                        params={"t":response_create_an_order.json()['track']})
                        #params = {"t":123}) проверка с несуществующим треком

response_get_an_order_by_number = get_an_order_by_number()
#print(response_get_an_order_by_number.json()) #расскоментировать для проверки