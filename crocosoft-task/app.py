from flask import Flask
from flask_restful import Api
# import sqlite3
from db import get_db , execute_query
from resources.customer import Customer
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'fares'
api = Api(app)

api.add_resource(Customer, '/customer/')#<string:name>')


@app.before_first_request
def seed():
    # connection = get_db()

    # cursor = connection.cursor()


    create_table = "CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY AUTOINCREMENT, name text , email text)"
    execute_query(create_table)


    return
if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
