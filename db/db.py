import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
client = app.test_client()


def db_con():
    return sqlite3.connect("server.db", check_same_thread=False)


sql = db_con()
sql.execute("""
    CREATE TABLE IF NOT EXISTS users(
     user_id INTEGER PRIMARY KEY NOT NULL,
     name VARCHAR,
     surname VARCHAR,
     age INTEGER,
     gender VARCHAR);
    """)

sql.commit()

user_id = input("ID: ")
name = input("Name: ")
surname = input("Surname: ")
age = input("Age: ")
gender = input("Gender: ")

sql.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?)", (user_id, name, surname, age, gender))
sql.commit()


@app.route('/api/users', methods=['GET'])
def get_users():
    response = sql.execute("SELECT * FROM users")
    query = response.fetchall()
    return jsonify(query)


# if request.method == "POST":
#     return {
#         'message': 'This endpoint should create an entity',
#         'method': request.method,
#         'body': request.json
#     }


@app.route('/basic_api/entities/<int:entity_id>', methods=['GET', 'PUT', 'DELETE'])
def entity(entity_id):
    if request.method == "GET":
        return {
            'id': entity_id,
            'message': 'This endpoint should return the entity {} details'.format(entity_id),
            'method': request.method
        }
    if request.method == "PUT":
        return {
            'id': entity_id,
            'message': 'This endpoint should update the entity {}'.format(entity_id),
            'method': request.method,
            'body': request.json
        }
    if request.method == "DELETE":
        return {
            'id': entity_id,
            'message': 'This endpoint should delete the entity {}'.format(entity_id),
            'method': request.method
        }


if __name__ == '__main__':
    app.run()
