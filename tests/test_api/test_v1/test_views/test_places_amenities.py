#!/usr/bin/python3
"""test cases for index route handlers"""
import unittest
import pep8
from flask import Flask
from api.v1.views import app_views
from api.v1.views import states
from models import storage
from models.state import State


class TestPlacesAmenitiesDocs(unittest.TestCase):
    """Class for testing documentation of the index routes handlers"""

    def test_pep8_conformance(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/places_amenities.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors")

    def test_pep8_conformance_test(self):
        """Test that tests/test_index.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files([
            'tests/test_api/test_v1/test_views/test_places_amenities.py'
        ])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors")

    def test_index_module_doc(self):
        """"""
        self.assertIsNotNone(states.__doc__)
