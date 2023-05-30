#!/usr/bin/python3
"""route handlers for Review object"""
from api.v1.views import app_views
from flask import abort, request, jsonify
from models import storage
from models.review import Review
from models.place import Place


@app_views.route('/places/<place_id>/reviews')
def reviews_get(place_id):
    """read all review object"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    reviews = place.reviews

    reviews = [review.to_dict() for review in reviews]
    return jsonify(reviews)


@app_views.route('/reviews/<review_id>')
def review_get(review_id):
    """for reading a review"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'])
def review_delete(review_id):
    """for deleting a review"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    storage.delete(review)
    storage.save()
    return jsonify({})


@app_views.route('/places/<place_id>/reviews', methods=["POST"])
def review_post(place_id):
    """for creating a review"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    if not request.is_json:
        return "Not a JSON", 400
    data = request.get_json()
    user_id = data.get('user_id')
    text = data.get('text')
    if not user_id:
        return "Missing user_id", 400
    if not text:
        return "Missing text", 400
    data["place_id"] = place_id
    review = Review(**data)
    review.save()
    return jsonify(review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=["PUT"])
def review_put(review_id):
    """
    for updating a review object
    """
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    if not request.is_json:
        return "Not a JSON", 400
    data = request.get_json()

    ignore = ('id', 'created_at', 'updated_at',
              'user_id', 'place_id')

    for key, value in data.items():
        if key in ignore:
            continue
        else:
            setattr(review, key, value)

    review.save()
    return jsonify(review.to_dict())
