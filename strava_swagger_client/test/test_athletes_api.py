# coding: utf-8

"""
    Strava API v3

    Strava API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.athletes_api import AthletesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAthletesApi(unittest.TestCase):
    """AthletesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.athletes_api.AthletesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_logged_in_athlete(self):
        """Test case for get_logged_in_athlete

        Get Authenticated Athlete  # noqa: E501
        """
        pass

    def test_get_logged_in_athlete_zones(self):
        """Test case for get_logged_in_athlete_zones

        Get Zones  # noqa: E501
        """
        pass

    def test_get_stats(self):
        """Test case for get_stats

        Get Athlete Stats  # noqa: E501
        """
        pass

    def test_update_logged_in_athlete(self):
        """Test case for update_logged_in_athlete

        Update Athlete  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()