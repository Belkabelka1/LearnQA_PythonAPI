import requests

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"key1":"value1"})
print(response.text)

response = requests.post("https://playground.learnqa.ru/api/check_type")
print(response.status_code)



