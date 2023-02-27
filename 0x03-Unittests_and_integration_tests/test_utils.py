#!/usr/bin/env python3
"""Unit test for the `utils.access_nested_map` function."""
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from utils import access_nested_map, get_json, memoize
from typing import Any, Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """Test the access_nested_map funtion in the utils module."""
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """Test the method returns what it is supposed to.

        Args:
            nested_map (Mapping): A nested map.
            path (Sequence): A sequence of keys representing the path
                             to the value.
            expected (Any): the correct result from the function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         expected: Any) -> None:
        """Test the method raises a `Key Error` in a given context.

        Args:
            nested_map (Mapping): A nested map.
            path (Sequence): A sequence of keys representing the path
                             to the value.
            expected (Any): the exception to be raised by the function.
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test the `get_json` function of the `utils` module."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that `utils.get_json` returns the expected result.

        Args:
            test_url (str): url to make request to.
            test_payload (Mapping): output of json method.
            Mock: MagicMock of `requests.get`
        """
        mock_get.return_value.json.return_value = test_payload
        self.assertDictEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test the `memoize` function in the `utils` module."""
    def test_memoize(self):
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
