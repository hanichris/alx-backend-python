#!/usr/bin/env python3
"""Unit test for the `utils.access_nested_map` function."""
import unittest
from parameterized import parameterized_class
from utils import access_nested_map


@parameterized_class(('map', 'path', 'expected'), [
    ({'a': 1}, ('a',), 1),
    ({'a': {'b': 2}}, ('a',), {'b': 2}),
    ({'a': {'b': 2}}, ('a', 'b'), 2)
])
class TestAccessNestedMap(unittest.TestCase):
    """Test the access_nested_map funtion in the utils module."""
    def test_access_nested_map(self):
        """test method returns what it is supposed to."""
        self.assertEqual(access_nested_map(self.map, self.path), self.expected)


if __name__ == "__main__":
    unittest.main()
