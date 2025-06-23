import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

# 1. Создаем задачу
response = requests.get(url)
response_data = response.json()
token = response_data["token"]
seconds = response_data["seconds"]
print(f"Задача создана. Токен: {token}, время ожидания: {seconds} секунд.")

# 2. Запрашиваем статус задачи ДО выполнения
response_before = requests.get(url, params={"token": token})
response_before_data = response_before.json()
print(f"Статус задачи до выполнения: {response_before_data}")

if "status" in response_before_data and response_before_data["status"] == "Job is NOT ready":
    print("Статус задачи до выполнения верен.")
else:
    print("Ошибка: Неверный статус задачи до выполнения.")

# 3. Ждем нужное количество секунд
print(f"Ожидаем {seconds} секунд...")
time.sleep(seconds)
print("Ожидание завершено.")

# 4. Запрашиваем статус задачи ПОСЛЕ выполнения
response_after = requests.get(url, params={"token": token})
response_after_data = response_after.json()
print(f"Статус задачи после выполнения: {response_after_data}")
