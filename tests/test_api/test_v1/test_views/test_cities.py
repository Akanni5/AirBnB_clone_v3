#!/usr/bin/python3
"""test cases for index route handlers"""
import unittest
import pep8
from flask import Flask
from api.v1.views import app_views
from api.v1.views import cities
from models import storage
from models.city import City
from models.state import State


class TestIndexDocs(unittest.TestCase):
    """Class for testing documentation of the index routes handlers"""

    def test_pep8_conformance(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/cities.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors")

    def test_pep8_conformance_test(self):
        """Test that tests/test_index.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files([
            'tests/test_api/test_v1/test_views/test_cities.py'
        ])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors")

    def test_index_module_doc(self):
        """"""
        self.assertIsNotNone(cities.__doc__)


class TestIndexRoutes(unittest.TestCase):
    """ class for testing routes and method for index.py """

    def setUp(self):
        """initialize flask instances"""
        self.app = Flask(__name__)
        self.app.register_blueprint(app_views)
        self.client = self.app.test_client()

    def test_get_city(self):
        """test get states"""
        # res = self.client.get('/api/v1/states')
        # self.assertEqual(res.status_code, 200)
        # self.assertTrue(res.is_json)
        # data = res.get_json()
        # self.assertEqual(len(data), storage.count(State))

    def test_get_cities(self):
        """test get state by id"""
        state = State(name="Lagos")
        state.save()
        city = City(name="Victoria Island", state_id=state.id)
        city.save()
        res = self.client.get('/api/v1/states/{}/cities'.format(state.id))
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.is_json)
        data = res.get_json()
        cities = state.cities
        self.assertEqual(len(data), len(cities))
        storage.delete(state)
        storage.delete(city)
        storage.close()
