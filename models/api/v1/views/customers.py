#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Customers """
from models.customers import Customer
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/customers', methods=['GET'], strict_slashes=False)
def get_customers():
    """
    Retrieves the list of all customer objects
    """
    users = storage.all(Customer).values()
    list_users = []
    for user in users:
        list_users.append(user.to_dict())
    return jsonify(list_users)


@app_views.route('/customer/<acct_num>', methods=['GET'], strict_slashes=False)
def get_customer(acct_num):
    """ Retrieves a customer """
    user = storage.get(Customer, acct_num)
    if not user:
        abort(404)

    return jsonify(user.to_dict())


@app_views.route('/customer/<acct_num>', methods=['DELETE'],
                 strict_slashes=False)
def delete_customer(acct_num):
    """
    Deletes a customer
    """

    user = storage.get(Customer, acct_num)

    if not user:
        abort(404)

    storage.delete(userr)
    storage.save()

    return make_response(jsonify(f"customer with {acct_num} deleted"), 200)


@app_views.route('/customers', methods=['POST'], strict_slashes=False)
def post_customer():
    """
    Creates a customer
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'first' not in request.get_json():
        abort (400, description="Missing first name")

    if 'last' not in request.get_json():
        abort (400, description="Missing last name")

    if 'dob' not in request.get_json():
        abort (400, description="Missing date of birth")

    if 'sex' not in request.get_json():
        abort (400, description="Missing sex")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")

    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    data = request.get_json()
    instance = Customer(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/customer/<acct_num>', methods=['PUT'], strict_slashes=False)
def put_customer(acct_num):
    """
    Updates a customer
    """
    user = storage.get(Customer, acct_num)

    if not user:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    accept = ['first', 'last', 'email', 'dob', 'sex', 'phone', 'addr']

    data = request.get_json()
    for key, value in data.items():
        if key in accept:
            setattr(customer, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)
