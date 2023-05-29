#!/usr/bin/python3
"""index route handlers"""

from flask import jsonify
from api.v1.views import app_views
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


@app_views.route('/status')
def index():
    """return OK as the status of the application"""
    data = {
        "status": "OK"
    }
    return jsonify(data)


@app_views.route('/stats')
def stats():
    """returns the storage objects counts"""
    users = storage.count(User)
    amenities = storage.count(Amenity)
    states = storage.count(State)
    places = storage.count(Place)
    reviews = storage.count(Review)
    cities = storage.count(City)

    data = {
        "amenities": amenities,
        "cities": cities,
        "places": places,
        "reviews": reviews,
        "states": states,
        "users": users,
    }

    return jsonify(data)
