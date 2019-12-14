from flask import Flask, request, jsonify
import pymongo
from random import random
from datetime import datetime

# MongoLab connection
client = pymongo.MongoClient("mongodb://test:aaaa12@ds253348.mlab.com:53348/docker-test-sd?retryWrites=false")
db = client["docker-test-sd"]

app = Flask(__name__)

# ********* AUTHENTICATION *********
@app.route('/auth/login', methods = ['POST'])
def login():
    user_collection = db['user']
    data = request.get_json(force=True)

    query = {'username': data['username']}
    count = 0
    result = user_collection.find(query)
    for user in result:
        count += 1

        if (user['password'] == data['password']):
            apikey = str(random()).split('.')[1]
            return_value = {
                'message': 'Successful login',
                'apikey': apikey,
                'status': 200
            }

            query = {'username': data['username']}
            new_values = {'$set': {"apikey": apikey}}

            user_collection.update_one(query, new_values)
        else:
            return_value = {
                'message': 'Wrong credentials',
                'status': 401
            }

    if (count == 0):
        return_value = {
            'message': 'Wrong credentials',
            'status': 401
        }
        
    print(return_value)
    return jsonify(return_value), return_value['status']

@app.route('/auth/logout', methods = ['POST'])
def logout():
    user_collection = db['user']
    data = request.get_json(force=True)

    query = {'username': data['username']}
    count = 0
    result = user_collection.find(query)
    for _ in result:
        count += 1

        return_value = {
            'message': 'Successful logout',
            'status': 200
        }

        query = {'username': data['username']}
        new_values = {'$set': {"apikey": ''}}

        user_collection.update_one(query, new_values)

    if (count == 0):
        return_value = {
            'message': 'Wrong credentials',
            'status': 401
        }
        
    print(return_value)
    return jsonify(return_value), return_value['status']

# ********* USERS *********
@app.route('/user/register', methods = ['POST'])
def user_register():
    user_collection = db['user']
    data = request.get_json(force=True)

    query = {'username': data['username']}
    count = 0
    result = user_collection.find(query)
    for _ in result:
        count += 1

    if (count == 0):
        user = {
            'username':  data['username'],
            'password':  data['password'],
            'apikey': ''
        }
        user_collection.insert_one(user)

        return_value = {
            'message': 'Successful register',
            'status': 200
        }
    else:
        return_value = {
            'message': 'The username is already registered',
            'status': 400
        }
        
    print(return_value)
    return jsonify(return_value), return_value['status']

@app.route('/user/delete', methods = ['POST'])
def user_delete():
    user_collection = db['user']
    task_collection = db['task']
    data = request.get_json(force=True)

    query = {'username': data['username']}
    count = 0
    result = user_collection.find(query)
    for _ in result:
        count += 1

        user_collection.delete_one(query)
        task_collection.delete_many(query)
        return_value = {
            'message': 'Successful deletion',
            'status': 200
        }

    if (count == 0):
        return_value = {
            'message': 'Wrong username',
            'status': 400
        }
        
    print(return_value)
    return jsonify(return_value), return_value['status']

# ********* TASKS *********
@app.route('/task', methods = ['POST'])
def tasks():
    user_collection = db['user']
    task_collection = db['task']
    data = request.get_json(force=True)

    query = {'username': data['username']}
    count = 0
    result = user_collection.find(query)
    for user in result:
        count += 1

        if (user['apikey'] == data['apikey']):
            tasks = task_collection.find(query,{ '_id': 0, 'id': 1, 'title': 1, 'detail': 1, 'date': 1, 'status': 1})
            return_tasks = []
            for task in tasks:
                return_tasks.append(task)

            return_value = {
                'tasks': return_tasks,
                'status': 200
            }
        else:
            return_value = {
            'message': 'Wrong credentials',
            'status': 401
        }

    if (count == 0):
        return_value = {
            'message': 'Wrong username',
            'status': 400
        }
        
    print(return_value)
    return jsonify(return_value), return_value['status']

@app.route('/task/<task_id>', methods = ['POST'])
def task(task_id):
    user_collection = db['user']
    task_collection = db['task']
    data = request.get_json(force=True)

    query = {'username': data['username']}
    count = 0
    result = user_collection.find(query)
    
    for user in result:
        count += 1

        if (user['apikey'] == data['apikey']):
            query['id'] = task_id
            tasks = task_collection.find(query,{ '_id': 0, 'id': 1, 'title': 1, 'detail': 1, 'date': 1, 'status': 1})
            return_task = []
            for task in tasks:
                return_task.append(task)

            return_value = {
                'task': return_task,
                'status': 200
            }
        else:
            return_value = {
            'message': 'Wrong credentials',
            'status': 401
        }

    if (count == 0):
        return_value = {
            'message': 'Wrong username',
            'status': 400
        }
        
    print(return_value)
    return jsonify(return_value), return_value['status']

@app.route('/task/add', methods = ['POST'])
def task_add():
    user_collection = db['user']
    task_collection = db['task']
    data = request.get_json(force=True)

    query = {'username': data['username']}
    count = 0
    result = user_collection.find(query)
    for user in result:
        count += 1

        if (user['apikey'] == data['apikey']):
            task = {
                'id': str(random()).split('.')[1],
                'title': data['title'],
                'detail': data['detail'],
                'date': datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                'status': 'NOT DONE',
                'username': data['username']
            }

            task_collection.insert_one(task)

            return_value = {
            'message': 'Successful adding',
            'status': 200
        }
        else:
            return_value = {
            'message': 'Wrong credentials',
            'status': 401
        }

    if (count == 0):
        return_value = {
            'message': 'Wrong username',
            'status': 400
        }
        
    print(return_value)
    return jsonify(return_value), return_value['status']

@app.route('/task/delete', methods = ['POST'])
def task_delete():
    user_collection = db['user']
    task_collection = db['task']
    data = request.get_json(force=True)

    query = {'username': data['username']}
    count = 0
    result = user_collection.find(query)
    for user in result:
        count += 1

        if (user['apikey'] == data['apikey']):
            query['id'] = data['task_id']

            task_collection.delete_one(query)

            return_value = {
            'message': 'Successful delete',
            'status': 200
        }
        else:
            return_value = {
            'message': 'Wrong credentials',
            'status': 401
        }

    if (count == 0):
        return_value = {
            'message': 'Wrong username',
            'status': 400
        }
        
    print(return_value)
    return jsonify(return_value), return_value['status']

@app.route('/task/status/<task_id>', methods = ['POST'])
def task_status(task_id):
    user_collection = db['user']
    task_collection = db['task']
    data = request.get_json(force=True)

    query = {'username': data['username']}
    count = 0
    result = user_collection.find(query)
    for user in result:
        count += 1

        if (user['apikey'] == data['apikey']):
            query['id'] = task_id

            status = 'NOT DONE' if (data['status'] == 0) else 'DONE'
            new_values = {'$set': {"status": status}}

            task_collection.update(query, new_values)

            return_value = {
            'message': 'Successful status change',
            'status': 200
        }
        else:
            return_value = {
            'message': 'Wrong credentials',
            'status': 401
        }

    if (count == 0):
        return_value = {
            'message': 'Wrong username',
            'status': 400
        }
        
    print(return_value)
    return jsonify(return_value), return_value['status']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)