import pytest

def test_phrase_shorter_than_15():
    """
    Тест запрашивает у пользователя фразу и проверяет, что она короче 15 символов.
    """
    # Запрашиваем фразу с помощью input()
    phrase = input("Set a phrase: ")

    # Проверяем, что длина фразы меньше 15 символов.
    assert len(phrase) < 15, f"Фраза '{phrase}' содержит 15 или более символов."