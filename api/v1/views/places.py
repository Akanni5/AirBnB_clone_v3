#!/usr/bin/python3
"""places view handler"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.city import City
from models.user import User


@app_views.route("/cities/<city_id>/places")
def places_get(city_id):
    """get all place objects from city"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    places = [place.to_dict() for place in city.places]
    return jsonify(places)


@app_views.route("places/<place_id>")
def place_get(place_id):
    """get place object"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route("places/<place_id>", methods=["DELETE"])
def place_delete(place_id):
    """delete place object"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    storage.delete(place)
    storage.save()
    return jsonify({})


@app_views.route("/cities/<city_id>/places", methods=["POST"])
def places_post(city_id):
    """create place object"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    if not request.is_json:
        return "Not a JSON", 400
    data = request.get_json()
    user_id = data.get('user_id')
    if not user_id:
        return "Missing user_id", 400
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    name = data.get('name')
    if not name:
        return "Missing name", 400
    data["city_id"] = city_id
    place = Place(**data)
    place.save()
    return jsonify(place.to_dict()), 201


@app_views.route("places/<place_id>", methods=["PUT"])
def places_put(place_id):
    """update place object"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    if not request.is_json:
        return "Not a JSON", 400
    ignore = ('id', 'created_at', 'update_at',
              'user_id', 'city_id')
    for key, val in request.get_json().items():
        if key in ignore:
            continue
        setattr(place, key, val)
    place.save()
    return jsonify(place.to_dict()), 200
