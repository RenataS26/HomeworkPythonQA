import pytest
from class_student import Class_student

@pytest.fixture
def db():
    db_connection_string = "postgresql://postgres:123@localhost:5432/postgres"
    db = Class_student(db_connection_string)
    return db  # обязательно вернуть объект

def test_new_student(db):  # <-- добавить фикстуру сюда в параметры
    user_email = "renkas@inbox.ru"
    subject_id = "1"
    user_id = "123"

    # создание
    creation_result = db.create(user_email, subject_id, user_id)
    assert creation_result is True or creation_result is not None, "Ошибка при создании студента"

    # изменение (меняем email)
    new_email = "new_email@inbox.ru"
    update_result = db.update(user_id, new_email=new_email)
    assert update_result is True, "Ошибка при обновлении студента"

    # удаление
    deletion_result = db.delete(user_id)
    assert deletion_result is True or deletion_result is not None, "Ошибка при удалении студента"
