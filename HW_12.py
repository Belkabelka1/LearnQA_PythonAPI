import requests
import pytest


def test_headers_print():

    url = "https://playground.learnqa.ru/api/homework_header"

    response = requests.get(url)
    headers = response.headers

    print(f"The values for given headers are {headers}")

    assert "x-secret-homework-header" in headers, "No 'x-secret-homework-header' in headers"