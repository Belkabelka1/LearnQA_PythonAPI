import requests

response = requests.post("https://playground.learnqa.ru/api/blala")
print(response.status_code)
print(response.text)