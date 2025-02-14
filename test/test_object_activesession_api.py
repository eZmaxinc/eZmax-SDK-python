# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.1
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from eZmaxApi.api.object_activesession_api import ObjectActivesessionApi


class TestObjectActivesessionApi(unittest.TestCase):
    """ObjectActivesessionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectActivesessionApi()

    def tearDown(self) -> None:
        pass

    def test_activesession_generate_federation_token_v1(self) -> None:
        """Test case for activesession_generate_federation_token_v1

        Generate a federation token
        """
        pass

    def test_activesession_get_current_v1(self) -> None:
        """Test case for activesession_get_current_v1

        Get Current Activesession
        """
        pass

    def test_activesession_get_current_v2(self) -> None:
        """Test case for activesession_get_current_v2

        Get Current Activesession
        """
        pass

    def test_activesession_get_list_v1(self) -> None:
        """Test case for activesession_get_list_v1

        Retrieve Activesession list
        """
        pass


if __name__ == '__main__':
    unittest.main()
