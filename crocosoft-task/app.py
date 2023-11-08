from flask import Flask
from flask_restful import Api
import sqlite3
from resources.customer import Customer
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'fares'
api = Api(app)

api.add_resource(Customer, '/customer/')#<string:name>')


@app.before_first_request
def seed():
    connection = sqlite3.connect('data.db')

    cursor = connection.cursor()

    # MUST BE INTEGER
    # This is the only place where int vs INTEGER matters—in auto-incrementing columns
    create_table = "CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY AUTOINCREMENT, name text , email text)"
    cursor.execute(create_table)

    connection.commit()

    connection.close()
    return
if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
