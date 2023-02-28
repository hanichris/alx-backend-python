#!/usr/bin/env python3
"""Unit test for the `client.py` module."""
from typing import Dict
import unittest
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
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


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class - Integration test of fixtures """
    @classmethod
    def setUpClass(cls):
        """method called before tests in an individual class are run"""
        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """ Integration test: public repos"""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """ Integration test for public repos with License """
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """method called after tests in an individual class have run"""
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
