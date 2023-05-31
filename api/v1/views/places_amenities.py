#!/usr/bin/python3
"""link between Place object and Amenity object"""

from flask import jsonify, abort
from api.v1.views import app_views
from models import storage, storage_t
from models.place import Place
from models.amenity import Amenity


@app_views.route('/places/<place_id>/amenities')
def amenities_get(place_id):
    """get all amenities linked to Place object"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    amenities = []
    if storage_t == 'db':
        amenities = place.amenities
        amenities = [amenity.to_dict() for amenity in amenities]
    else:
        amenities = place.amenity_ids
    return jsonify(amenities)


@app_views.route(
    '/places/<place_id>/amenities/<amenity_id>',
    methods=["DELETE"]
)
def place_amenity_delete(place_id, amenity_id):
    """remove link between place and amenity """
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)
    if not place:
        abort(404)
    if not amenity:
        abort(404)
    is_linked = False
    if storage_t == 'db':
        if amenity in place.amenities:
            is_linked = True
            place.amenities.remove(amenity)
    else:
        if amenity.id in place.amenity_ids:
            is_linked = True
            place.amenity_ids.remove(amenity.id)
    if not is_linked:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({})


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=["POST"])
def place_amenity_post(place_id, amenity_id):
    """link Amenity object to a Place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if storage_t == 'db':
        if amenity in place.amenities:
            return jsonify(amenity.to_dict())
        place.amenities.append(amenity)
    else:
        if amenity.id in place.amenity_ids:
            return jsonify(amenity.to_dict())
        place.amenity_ids.append(amenity.id)
    return jsonify(amenity.to_dict()), 201
