import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


def create_database():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                         id INTEGER PRIMARY KEY,
                         service_name TEXT NOT NULL,
                         username TEXT NOT NULL,
                         password TEXT NOT NULL)''')
    conn.commit()
    conn.close()