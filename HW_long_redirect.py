import requests

response = requests.get('https://playground.learnqa.ru/api/long_redirect', allow_redirects=True)
redirect_count = len(response.history)
last_url = response

print(f"Количество редиректов: {redirect_count}")
print(f"Конечный URL: {last_url.url}")

