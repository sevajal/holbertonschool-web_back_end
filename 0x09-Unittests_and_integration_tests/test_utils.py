#!/usr/bin/env python3
""" Parameterize a unit test  """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Any, Dict


class TestAccessNestedMap(unittest.TestCase):
    """ Test Access Nested Map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, answer) -> Any:
        """ Test correct answers for access nested map """
        self.assertEqual(access_nested_map(nested_map, path), answer)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path) -> Any:
        """ Test the access nested map exceptions """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Test the method utils.get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock) -> Any:
        """ Test the method utils.get_json with patch """
        mock.return_value = test_payload
        response = get_json(test_url)
        self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """ Test the method Memoize """
    def test_memoize(self):
        """ Test the method Memoize """
        class TestClass:
            """ Test class """
            def a_method(self):
                """ method that return 42 """
                return 42

            @memoize
            def a_property(self):
                """ a_property method """
                return self.a_method()

        with patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mockMethod.assert_called_once
