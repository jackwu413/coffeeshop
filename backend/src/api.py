import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)
db_drop_and_create_all()

## ROUTES

@app.route('/drinks', methods=['GET'])
def get_drinks(): 
    drinks = Drink.query.all()
    return jsonify({
        'success': True, 
        'drinks': [drink.short() for drink in drinks]
    }), 200


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drink_detail(payload): 
    drinks = Drink.query.all()
    return jsonify({
        'success': True, 
        'drinks': [drink.long() for drink in drinks]
    }), 200

'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def add_drink(payload):
    body = request.get_json()

    new_drink = Drink(
        title = body['title'], 
        recipe = body['recipe']
    )

    new_drink.insert()
    return jsonify({
        'success': True, 
        'drinks': Drink.long(new_drink)
    }), 200


'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(payload, id): 
    body = request.get_json()
    drink = Drink.query.filter(Drink.id == id).one_or_none()

    if not drink: 
        abort(400)

    try: 
        title = body.get('title')
        recipe = body.get('recipe')

        if title: 
            drink.title = title 

        if recipe: 
            drink.recipe = recipe 

    except: 
        abort(400)

    return jsonify({
        'success': True, 
        'drinks': [drink.long()]
    }), 200

'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(payload, id): 
    drink = Drink.query.filter(Drink.id == id).one_or_none()

    if not drink: 
        abort(404) 

    try: 
        drink.delete()
    except: 
        abort(400)

    return jsonify({
        'success': True, 
        'delete': id
    }), 200

## Error Handling
'''
Example error handling for unprocessable entity
'''
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422


@app.errorhandler(404) 
def not_found(error): 
    return jsonify({
        'success': False, 
        'error': 404, 
        'message': 'recource not found'
    }), 404



@app.errorhandler(AuthError)
def auth_error(error): 
    return jsonify({
        'success': False, 
        'error': error.status_code, 
        'message': error.error['description']
    }), error.status_code

@app.errorhandler(401) 
def unauthorized(error): 
    return jsonify({
        'success': False, 
        'error': 401, 
        'message': 'Unauthorized'
    }), 401

@app.errorhandler(500) 
def internal_server_error(error): 
    return jsonify({
        'success': False, 
        'error': 500, 
        'message': 'Internal server error'
    }), 500
@app.errorhandler(400) 
def bad_request(error): 
    return jsonify({
        'success': False, 
        'error': 400, 
        'message': 'bad request'
    }), 400

@app.errorhandler(405) 
def method_not_allowed(error): 
    return jsonify({
        'success': False, 
        'error': 405, 
        'message': 'method not allowed'
    }), 405