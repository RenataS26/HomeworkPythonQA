import requests

def test_create_project():
    url = "https://yougile.com/api-v2/projects"  
    headers = {
        "Authorization": "Bearer QGxajL-FieVKlECClZRYChyIY23fFop8mBTaS3cIn-YSooDd9deoUyiJ26QAxmqD", 
        "Content-Type": "application/json"
    }
    payload = {
        "title": "МозгКипит",
        "users": {
            '095bb009-1096-4522-8b2d-310432dcb02e': 'admin',
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 201 or response.status_code == 200, f"Ошибка создания проекта: {response.status_code} {response.text}"
    data = response.json()
    assert "id" in data, "В ответе отсутствует ID проекта"

    print("Тест пройден")

if __name__ == "__main__":
    test_create_project()

# негативный тест отсутствует title
def test_create_negative_project():
    url = "https://yougile.com/api-v2/projects"  
    headers = {
        "Authorization": "Bearer QGxajL-FieVKlECClZRYChyIY23fFop8mBTaS3cIn-YSooDd9deoUyiJ26QAxmqD", 
        "Content-Type": "application/json"
    }
    payload = {
        "title": "",
        "users": {
            '095bb009-1096-4522-8b2d-310432dcb02e': 'admin',
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 400 or response.status_code == 400, f"Ошибка создания проекта: {response.status_code} {response.text}"
   
    print("Тест пройден")

if __name__ == "__main__":
    test_create_project() 