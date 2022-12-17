import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""
    CREATE TABLE IF NOT EXISTS people(
     user_id INTEGER,
     name VARCHAR,
     surname VARCHAR,
     age INTEGER,
     gender VARCHAR);
    """)

db.commit()

user_id = input("ID: ")
name = input("Name: ")
surname = input("Surname: ")
age = input("Age: ")
gender = input("Gender: ")

sql.execute("SELECT user_id FROM people")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO people VALUES (?, ?, ?, ?, ?)", (user_id, name, surname, age, gender))
    db.commit()
    print("Пользователь создан!")
else:
    print("Такой пользователь уже есть!")
