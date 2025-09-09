from sqlalchemy import create_engine, text

class Class_student:
    scripts = {
        "delete_user_id": text("DELETE FROM users WHERE user_id=:user_id"),
        "insert_new": text("INSERT INTO users (user_email, subject_id, user_id) VALUES (:email, :subject_id, :user_id)"),
        "update_email": text("UPDATE users SET user_email = :email WHERE user_id = :user_id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create(self, user_email, subject_id, user_id):
        try:
            with self.__db.connect() as conn:
                with conn.begin():
                    conn.execute(self.scripts["insert_new"], {"email": user_email, "subject_id": subject_id, "user_id": user_id})
            return True
        except Exception as e:
            print("Ошибка создания студента:", e)
            return False

    def update(self, user_id, new_email=None):
        if not new_email:
            return False
        try:
            with self.__db.connect() as conn:
                with conn.begin():
                    conn.execute(self.scripts["update_email"], {"user_id": user_id, "email": new_email})
            return True
        except Exception as e:
            print("Ошибка обновления студента:", e)

            return False

    def delete(self, user_id):
        try:
            with self.__db.connect() as conn:
                with conn.begin():
                    conn.execute(self.scripts["delete_user_id"], {"user_id": user_id})
            return True
        except Exception as e:
            print("Ошибка удаления студента:", e)
            return False

           
                                    