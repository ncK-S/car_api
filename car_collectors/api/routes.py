from flask import Blueprint, jsonify, request

from car_collectors.helpers import token_required
from car_collectors.models import db, User, Car,car_schema, cars_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('getdata')
@token_required
def getdata():
    return {'some': 'value'}

@api.route('/cars', methods=['POST'])
@token_required
def create_car(current_user_token):
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    mileage = request.json['mileage']
    dimensions = request.json['dimensions']
    weight = request.json['weight']
    cost_of_production = request.json['cost_of_production']
    series = request.json['series']
    user_token = current_user_token.token

    car = Car(name, description,price ,dimensions,
                weight,cost_of_production,series,user_token)
    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(Car)
    return jsonify(response)

# retrieve all cars
@api.route('/cars', methods=['GET'])
@token_required
def get_cars(current_user_token):
    owner= current_user_token.token
    cars = Car.query.filter_by(user_token = owner).all()
    response = cars_schema.dump(Car)
    return jsonify(response)

# retrieve a single car
@api.route('/cars/<id>', methods=['GET'])
@token_required
def get_car(current_user_token, id):
    owner= current_user_token.token
    car = Car.query.get(id)
    response = car_schema.dump(car)
    return jsonify(response)

# update car
@api.route('/car/<id>', methods=['POST', 'PUT'])
@token_required
def update_car(current_user_token, id):
    car = Car.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    mileage = request.json['mileage']
    dimensions = request.json['dimensions']
    weight = request.json['weight']
    cost_of_production = request.json['cost_of_production']
    series = request.json['series']
    user_token = current_user_token.token


    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)

# DELETE a car
@api.route('/cars/<id>', methods = ['DELETE'])
@token_required
def delete_car(current_user_token, id):
    car = Car.query.get(id)
    db.sessoin.delete(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)

