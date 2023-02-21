#!/usr/bin/env python3
""" Parameterize a unit test  """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map
from typing import Any


class TestAccessNestedMap(unittest.TestCase):
    """ Test Access Nested Map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, answer) -> Any:
        """ Test answers for access nested map """
        self.assertEqual(access_nested_map(nested_map, path), answer)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path) -> Any:
        """ Test the access nested map exceptions """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
