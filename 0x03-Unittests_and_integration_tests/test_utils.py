#!/usr/bin/env python3
"""Unit test for the `utils.access_nested_map` function."""
import unittest
from parameterized import parameterized
from utils import access_nested_map
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
                             to the value
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
