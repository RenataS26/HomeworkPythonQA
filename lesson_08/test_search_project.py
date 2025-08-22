import requests

BASE_URL = "https://yougile.com/api-v2/" # Замените на реальный URL API
IP_TO_SEARCH = "ed10eb0a-2bb5-4b5d-8c8f-4c12a597c90c"  # Пример IP для поиска
token= "QGxajL-FieVKlECClZRYChyIY23fFop8mBTaS3cIn-YSooDd9deoUyiJ26QAxmqD"

def test_search_company_by_ip():
    headers = {
        "Authorization": f"Bearer {token}", 
        "Content-Type": "application/json"
    }
    params = {"ip": IP_TO_SEARCH}
    response = requests.get(f"{BASE_URL}projects/{IP_TO_SEARCH}", params=params, headers=headers)

    assert response.status_code == 200, f"Ошибка: ожидается 200, получено {response.status_code}"

    data = response.json()

    # Проверяем ключи и типы данных
    assert "id" in data and isinstance(data["id"], str), "Отсутствует или неверен 'id'"
    assert "title" in data and isinstance(data["title"], str), "Отсутствует или неверен 'title'"
    assert "timestamp" in data and isinstance(data["timestamp"], int), "Отсутствует или неверен 'timestamp'"
    

    print("API тест успешно пройден. Ответ корректен.")

if __name__ == "__main__":
    test_search_company_by_ip()

#негативный тест метод запроса DELETE  
def test_search_project_negative():
    headers = {
        "Authorization": f"Bearer {token}", 
        "Content-Type": "application/json"
    }
    # Пытаемся отправить DELETE-запрос на endpoint предназначенный для GET
    response = requests.delete(f"{BASE_URL}projects/{IP_TO_SEARCH}", headers=headers)

    assert response.status_code in (400, 404, 405), \
        f"Ожидается ошибка 400, 404 или 405, получен {response.status_code}"

    print(f"Негативный тест успешен. Метод PUT на GET endpoint вернул {response.status_code}.")

if __name__ == "__main__":
    test_search_project_negative()
