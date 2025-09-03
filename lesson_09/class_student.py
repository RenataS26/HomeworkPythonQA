from sqlalchemy import create_engine, text

class Class_student:
    scripts = {
        "delete_user_id": text("DELETE FROM users WHERE user_id=:user_id"),
        "insert_new": text("INSERT INTO users (user_email, subject_id, user_id) VALUES (:new_user_email, :new_subject_id, :new_user_id)")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create(self, user_email, subject_id, user_id):
        with self.__db.connect() as conn:
            with conn.begin():
                conn.execute(self.scripts["insert_new"], {
                    "new_user_email": user_email,
                    "new_subject_id": subject_id,
                    "new_user_id": user_id
                })

    def delete(self, user_id):
        with self.__db.connect() as conn:
            with conn.begin():
                conn.execute(self.scripts["delete_user_id"], {"user_id": user_id})
                                    