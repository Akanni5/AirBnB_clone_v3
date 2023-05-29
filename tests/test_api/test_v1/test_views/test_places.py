#!/usr/bin/python3
"""test cases for index route handlers"""
import unittest
import pep8
from flask import Flask
from api.v1.views import app_views
from api.v1.views import places
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.user import User


class TestPlaceDocs(unittest.TestCase):
    """Class for testing documentation of the index routes handlers"""

    def test_pep8_conformance(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/places.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors")

    def test_pep8_conformance_test(self):
        """Test that tests/test_index.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files([
            'tests/test_api/test_v1/test_views/test_places.py'
        ])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors")

    def test_index_module_doc(self):
        """"""
        self.assertIsNotNone(places.__doc__)


class TestPlacesRoutes(unittest.TestCase):
    """ class for testing routes and method for index.py """

    def setUp(self):
        """initialize flask instances"""
        self.app = Flask(__name__)
        self.app.register_blueprint(app_views)
        self.client = self.app.test_client()

    def test_post_places(self):
        """create a new place"""
        user = User(email="user1@demo.com", password="user1")
        user.save()
        state = State(name="lagos")
        state.save()
        city = City(name="Surulere", state_id=state.id)
        city.save()

        place_data = {
            "name": "national stadium",
            "user_id": user.id,
        }

        res = self.client.post('api/v1/cities/{}/places'.format(
            city.id
        ), json=place_data)

        self.assertEqual(res.status_code, 201)
        place_data = res.get_json()
        place = storage.get(Place, place_data.get('id'))
        self.assertIsNotNone(place)
        res = self.client.get('api/v1/places/{}'.format(
            place.id
        ))
        self.assertEqual(res.status_code, 200)
        storage.delete(city)
        storage.delete(state)
        storage.delete(user)
        storage.delete(place)
        storage.close()
