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
        """Test that `GithubOrgClient.org` returns the correct value.

        Args:
            test_org (str): name of the organisation.
            mock_get (MagicMock): created mock object.
        """
        client = GithubOrgClient(test_org)
        _url = client.ORG_URL.format(org=test_org)
        client.org()
        mock_get.assert_called_once_with(_url)

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_public_repos_url(self, test_org: str):
        """Test the `GithubOrgClient._public_repos_url` method.

        Args:
            test_org (str): test organisation.
        """
        payload = {'repos_url':  f"https://api.github.com/orgs/{test_org}"}
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock,
                   return_value=payload):
            client = GithubOrgClient('google')
            self.assertEqual(client._public_repos_url, payload['repos_url'])


if __name__ == "__main__":
    unittest.main()
