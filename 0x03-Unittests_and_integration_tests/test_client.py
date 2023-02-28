#!/usr/bin/env python3
"""Unit test for the `client.py` module."""
from typing import Dict
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get):
        """Test `GithubOrgClient.public_repos` method."""

        mock_payload = [{'name': 'first_repo'},
                        {'name': 'second_repo'}]
        mock_get.return_value = mock_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos:
            mock_public_repos.return_value = ['first_repo', 'second_repo']
            client = GithubOrgClient('not_real_org')
            resp = client.public_repos()

            self.assertEqual(resp, mock_public_repos.return_value)
            mock_get.assert_called_once()
            mock_public_repos.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo: Dict[str, Dict],
                         key: str, expected: bool) -> None:
        """Test `GithubOrgClient.has_license` method.

        Args:
            repo (dict): repository representation.
            key (str): license for the repo.
            expected (bool): expected output.
        """
        has_license = GithubOrgClient.has_license(repo, key)
        self.assertIs(has_license, expected)


if __name__ == "__main__":
    unittest.main()
