#!/usr/bin/python3
"""test cases for index route handlers"""
import unittest
import pep8
from flask import Flask
from api.v1.views import app_views
from api.v1.views import index
from models import storage


class TestIndexDocs(unittest.TestCase):
    """Class for testing documentation of the index routes handlers"""

    def test_pep8_conformance(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/index.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors")

    def test_pep8_conformance_test(self):
        """Test that tests/test_index.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files([
            'tests/test_api/test_v1/test_views/test_index.py'
        ])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors")

    def test_index_module_doc(self):
        """"""
        self.assertIsNotNone(index.__doc__)


class TestIndexRoutes(unittest.TestCase):
    """ class for testing routes and method for index.py """

    def setUp(self):
        """initialize flask instances"""
        self.app = Flask(__name__)
        self.app.register_blueprint(app_views)
        self.client = self.app.test_client()

    def test_get_status(self):
        """test status endpoint"""
        res = self.client.get('/api/v1/status/1')
        self.assertEqual(res.status_code, 404)
        res = self.client.get('/api/v1/status')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.is_json)
        data = res.get_json()
        self.assertEqual(data.get('status'), "OK")

    def test_get_stats(self):
        """test stats endpoint"""
        res = self.client.get('/api/v1/stats')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.is_json)
        data = res.get_json()
        total_obj = 0
        all_obj = storage.count()
        for val in data.values():
            total_obj += val
        self.assertTrue(total_obj, all_obj)
