#!/usr/bin/env python3
""" Parameterize and patch as decorators """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """ Test GithubOrgClient """
    @parameterized.expand([
        ("google"),
        ("abc"),
        ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, mock):
        """ Test GithubOrgClient.org """
        test_client = GithubOrgClient(org_name)
        test_return = test_client.org
        self.assertEqual(test_return, mock.return_value)
        mock.assert_called_once

    def test_public_repos_url(self):
        """ Test GithubOrgClient._public_repos_url """
        with patch.object(GithubOrgClient, "org", new_callable=PropertyMock,
                          return_value={"repos_url": "sevajal"}) as mock:
            test_json = {"repos_url": "sevajal"}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            test_return = test_client._public_repos_url
            mock.assert_called_once
            self.assertEqual(test_return, mock.return_value.get("repos_url"))

    @patch("client.get_json", return_value=[{"name": "sevajal"}])
    def test_public_repos(self, mock_get):
        """ Test GithubOrgClient._public_repos """
        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_prop:
            test_client = GithubOrgClient("sevajal")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["sevajal"])
            mock_get.assert_called_once
            mock_prop.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, license_key, expected_return):
        """ Test GithubOrgClient.has_license """
        test_client = GithubOrgClient("sevajal")
        test_return = test_client.has_license(repo, license_key)
        self.assertEqual(expected_return, test_return)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test Integration GithubOrgClient """
    @classmethod
    def setUpClass(cls):
        """ SetUp class method """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """ TearDown Class method"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Test GithubOrgClient.public_repos """
        test_client = GithubOrgClient("sevajal")
        assert True

    def test_public_repos_with_license(self, license="apache-2.0"):
        """ Test the public_repos with license """
        test_client = GithubOrgClient("sevajal")
        assert True
