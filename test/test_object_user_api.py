# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.0
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from eZmaxApi.api.object_user_api import ObjectUserApi


class TestObjectUserApi(unittest.TestCase):
    """ObjectUserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectUserApi()

    def tearDown(self) -> None:
        pass

    def test_user_create_object_v1(self) -> None:
        """Test case for user_create_object_v1

        Create a new User
        """
        pass

    def test_user_edit_object_v1(self) -> None:
        """Test case for user_edit_object_v1

        Edit an existing User
        """
        pass

    def test_user_edit_permissions_v1(self) -> None:
        """Test case for user_edit_permissions_v1

        Edit multiple Permissions
        """
        pass

    def test_user_get_apikeys_v1(self) -> None:
        """Test case for user_get_apikeys_v1

        Retrieve an existing User's Apikeys
        """
        pass

    def test_user_get_autocomplete_v2(self) -> None:
        """Test case for user_get_autocomplete_v2

        Retrieve Users and IDs
        """
        pass

    def test_user_get_effective_permissions_v1(self) -> None:
        """Test case for user_get_effective_permissions_v1

        Retrieve an existing User's Effective Permissions
        """
        pass

    def test_user_get_list_v1(self) -> None:
        """Test case for user_get_list_v1

        Retrieve User list
        """
        pass

    def test_user_get_object_v2(self) -> None:
        """Test case for user_get_object_v2

        Retrieve an existing User
        """
        pass

    def test_user_get_permissions_v1(self) -> None:
        """Test case for user_get_permissions_v1

        Retrieve an existing User's Permissions
        """
        pass

    def test_user_get_subnets_v1(self) -> None:
        """Test case for user_get_subnets_v1

        Retrieve an existing User's Subnets
        """
        pass

    def test_user_send_password_reset_v1(self) -> None:
        """Test case for user_send_password_reset_v1

        Send password reset
        """
        pass


if __name__ == '__main__':
    unittest.main()
