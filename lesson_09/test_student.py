from class_student import Class_student

def test_new_student():
    db_connection_string = "postgresql://postgres:123@localhost:5432/postgres"
    db = Class_student(db_connection_string)

    user_email = "renkas@inbox.ru"
    subject_id = "1"
    user_id = "123"

    # создание
    db.create(user_email, subject_id, user_id)

    #удаление
    db.delete(user_id)