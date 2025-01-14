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

from eZmaxApi.api.object_apikey_api import ObjectApikeyApi


class TestObjectApikeyApi(unittest.TestCase):
    """ObjectApikeyApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectApikeyApi()

    def tearDown(self) -> None:
        pass

    def test_apikey_create_object_v2(self) -> None:
        """Test case for apikey_create_object_v2

        Create a new Apikey
        """
        pass

    def test_apikey_edit_object_v1(self) -> None:
        """Test case for apikey_edit_object_v1

        Edit an existing Apikey
        """
        pass

    def test_apikey_edit_permissions_v1(self) -> None:
        """Test case for apikey_edit_permissions_v1

        Edit multiple Permissions
        """
        pass

    def test_apikey_generate_delegated_credentials_v1(self) -> None:
        """Test case for apikey_generate_delegated_credentials_v1

        Generate a delegated credentials
        """
        pass

    def test_apikey_get_cors_v1(self) -> None:
        """Test case for apikey_get_cors_v1

        Retrieve an existing Apikey's cors
        """
        pass

    def test_apikey_get_list_v1(self) -> None:
        """Test case for apikey_get_list_v1

        Retrieve Apikey list
        """
        pass

    def test_apikey_get_object_v2(self) -> None:
        """Test case for apikey_get_object_v2

        Retrieve an existing Apikey
        """
        pass

    def test_apikey_get_permissions_v1(self) -> None:
        """Test case for apikey_get_permissions_v1

        Retrieve an existing Apikey's Permissions
        """
        pass

    def test_apikey_get_subnets_v1(self) -> None:
        """Test case for apikey_get_subnets_v1

        Retrieve an existing Apikey's subnets
        """
        pass

    def test_apikey_regenerate_v1(self) -> None:
        """Test case for apikey_regenerate_v1

        Regenerate the Apikey
        """
        pass


if __name__ == '__main__':
    unittest.main()
