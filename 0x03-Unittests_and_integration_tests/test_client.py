#!/usr/bin/env python3
"""Unit test for the `client.py` module."""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Test the `GithubOrgClient` class."""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, test_org: str, mock_get) -> None:
        """Test that GithubOrgClient.org returns the correct value.

        Args:
            test_org (str): name of the organisation.
            mock_get (MagicMock): created mock object.
        """
        client = GithubOrgClient(test_org)
        _url = client.ORG_URL.format(org=test_org)
        client.org()
        mock_get.assert_called_once_with(_url)


if __name__ == "__main__":
    unittest.main()
