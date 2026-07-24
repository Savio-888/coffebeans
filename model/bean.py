from model.database import Database
from sqlite3 import Error
class Bean:
    @staticmethod
    def create_table():
        try:
            conn = Database.connect_db()
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS beans(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, brewing TEXT, rating INTEGER CHECK(rating BETWEEN 1 AND 10), date_create TEXT NOT NULL DEFAULT(CURRENT_TIMESTAMP))')
            conn.commit()
            conn.close()
            return True
        except Error as e:
            print(f'ERROR: {e}')
            conn.rollback()
            conn.close()
            return False
    @staticmethod
    def insert_bean(name, brewing, rating):
        try:
            conn = Database.connect_db()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO beans(name, brewing, rating) VALUES(?, ?, ?)', (name, brewing, rating))
            conn.commit()
            conn.close()
            return True
        except Error as e:
            print(f'ERROR: {e}')
            conn.rollback()
            conn.close()
            return False
    @staticmethod
    def list_beans():
        try:
            conn = Database.connect_db()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM beans')
            if cursor.fetchall():
                db_list = cursor.fetchall
                actual_list = [dict(line) for line in db_list]
                return actual_list
            else:
                return False
        except Error as e:
            print(f'ERROR: {e}')
            conn.rollback()
            conn.close()
            return False
    @staticmethod
    def list_byrating_best():
        try:
            conn = Database.connect_db()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM beans ORDER BY rating DESC')
            if cursor.fetchall():
                db_list = cursor.fetchall
                actual_list = [dict(line) for line in db_list]
                return actual_list
            else:
                return False
        except Error as e:
            print(f'ERROR: {e}')
            conn.rollback()
            conn.close()
            return False
    @staticmethod
    def list_byrating_worst():
        try:
            conn = Database.connect_db()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM beans ORDER BY rating ASC')
            if cursor.fetchall():
                db_list = cursor.fetchall
                actual_list = [dict(line) for line in db_list]
                return actual_list
            else:
                return False
        except Error as e:
            print(f'ERROR: {e}')
            conn.rollback()
            conn.close()
            return False
    @staticmethod
    def list_bydate():
        try:
            conn = Database.connect_db()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM beans ORDER BY date_create DESC')
            if cursor.fetchall():
                db_list = cursor.fetchall
                actual_list = [dict(line) for line in db_list]
                return actual_list
            else:
                return False
        except Error as e:
            print(f'ERROR: {e}')
            conn.rollback()
            conn.close()
            return False
