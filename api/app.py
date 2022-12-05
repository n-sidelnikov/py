from flask import Flask, jsonify, request

app = Flask(__name__)

client = app.test_client()

people = [
    {
        'name': 'Ivan',
        'profession': 'QA'
    }
]


@app.route('/list', methods=['GET'])
def get():
    return jsonify(people)


@app.route('/add', methods=['POST'])
def add():
    req = request.json
    people.append(req)
    return jsonify(people)


@app.route('/edit/...', methods=['PUT'])
def edit():
    pass


@app.route('/delete/...', methods=['DELETE'])
def delete():
    pass


if __name__ == '__main__':
    app.run()

# tasks
# 1. add new handlers (edit, delete)
# 2(3). add database (sqlite) - table users (id, email, name, gender)
# 3(2). write tests for aforementioned handlers (1 positive, 1 negative)
# 4. write helper fixtures to create test data - valid user, woman user

# requirements
# can use some information
