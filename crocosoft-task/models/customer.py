from flask_restful import Resource, reqparse
import sqlite3
from flask import request
from db import get_db   , execute_query



class CustomerModel():
    TABLE_NAME = 'customers'

    def __init__(self , id, name, email):
        self.id = id
        self.name = name
        self.email = email


    @classmethod
    def find_by_id(cls, _id):
        connection = get_db()
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
        try:
            result = cursor.execute(query, (_id,))
            row = result.fetchone()
            temp = row
            if row:
                user = cls(*row)
            else:
                user = None


            connection.close()
            return user
        except Exception as e:
            return str(e)

    @classmethod
    def insert(cls, customer):

        query = "INSERT INTO {table} (name  , email) VALUES(? , ?)".format(table=cls.TABLE_NAME)

        execute_query(query,(customer['name'],customer["email"]))

        return

    @classmethod
    def update(cls, customer):

        query = "UPDATE {table} SET  email =? WHERE id=?".format(table=cls.TABLE_NAME)
        execute_query(query, ( customer["email"],customer['id']))


        return
    @classmethod
    def delete(cls):
        id = request.get_json()['id']

        query = "DELETE FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)

        execute_query(query,(id,))



        return

    def json(self):

        return { "id":self.id,'name': self.name, "email":self.email}
