from flask_restful import Resource, reqparse
from flask import request , json
from models.customer import CustomerModel


class Customer(Resource):

    @classmethod
    def get(cls):
        cust = CustomerModel.find_by_id(request.get_json()["id"])
        if not cust:
            return {'message': 'Customer Not Found'}, 404
        return cust.json(), 200

    @classmethod
    def post(cls):
        temp = request.get_json()
        print(temp)
        cust = CustomerModel.insert(temp)
        return {"message":"Customer created successfully"} , 201

    @classmethod
    def put(cls):
        cust = CustomerModel.find_by_id(request.get_json()["id"])
        temp = request.get_json()
        if not cust:
            return {'message': 'Customer Not Found'} , 404
        cust = CustomerModel.update(temp)
        # i returned HTTP 200 insted of 204 for the message to be displayed
        return {'message': 'Customer updated'} , 200

    @classmethod
    def delete(cls):
        cust = CustomerModel.find_by_id(request.get_json()["id"])
        if not cust:
            return {'message': 'Customer Not Found'} , 404
        cust.delete()
        #i returned HTTP 200 insted of 204 for the message to be displayed
        return {'message': 'customer deleted'} , 200
