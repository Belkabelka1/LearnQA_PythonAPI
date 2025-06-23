import requests

#запрос без параметра метод. Выводится <Response [400]>
responce = requests.request(method='', url='https://playground.learnqa.ru/ajax/api/compare_query_type')
print(responce)

#запрос с параметром не из списка. Выводится <Response [400]>
responce = requests.request(method='PATCH', url='https://playground.learnqa.ru/ajax/api/compare_query_type')
print(responce)

#запрос с правильным параметром. Выводится <Response [200]>
responce = requests.request(method='GET', url='https://playground.learnqa.ru/ajax/api/compare_query_type')
print(responce)

#проверка сочетания реальных типов запроса и значений параметра method
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
methods = ['GET', 'POST', 'PUT', 'DELETE']
results = {}
for http_method in ['GET', 'POST', 'PUT', 'DELETE']:
    for method_value in methods:
        payload = {}
        if http_method == 'GET':
            payload = {'method': method_value}
        else:
            payload = {'method': method_value}
        # Отправка запроса с указанными параметрами
        response = requests.request(method=http_method, url=url, params=payload, data=payload)

        # Формирование ключа для хранения результата, включающего HTTP-метод и значение method
        key = f"{http_method}|{method_value}"
        results[key] = {
            "status_code": response.status_code,
            "http_method": http_method,
            "method_value": method_value,
            "text": response.text
        }

# Вывод результатов для анализа
print("Результаты запросов:")
for key, data in results.items():
    print(f"\n{key}:")
    print(f"  HTTP-метод: {data['http_method']}")
    print(f"  Значение параметра method: {data['method_value']}")
    print(f"  Код ответа: {data['status_code']}")
    print("  Ответ сервера:")
    print(data['text'])