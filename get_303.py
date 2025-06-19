import requests

response = requests.post("https://playground.learnqa.ru/api/get_303", allow_redirects=True)
print(response.status_code)