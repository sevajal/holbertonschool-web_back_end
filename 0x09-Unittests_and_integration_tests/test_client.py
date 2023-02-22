#!/usr/bin/env python3
""" Parameterize and patch as decorators """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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
