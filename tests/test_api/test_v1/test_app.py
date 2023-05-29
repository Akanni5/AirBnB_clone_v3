#!/usr/bin/python3
"""test cases for app.py"""
import unittest
import pep8


class TestAppDocs(unittest.TestCase):
    """ Test cases for application documentation """

    def test_pep8_conformance(self):
        """Test that app.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/app.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors"
        )

    def test_pep8_conformance_test(self):
        """Test that test_app.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(
            ['tests/test_api/test_v1/test_app.py']
        )
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors")
