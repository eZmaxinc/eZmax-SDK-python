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

from eZmaxApi.api.scim_users_api import ScimUsersApi


class TestScimUsersApi(unittest.TestCase):
    """ScimUsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ScimUsersApi()

    def tearDown(self) -> None:
        pass

    def test_users_create_object_scim_v2(self) -> None:
        """Test case for users_create_object_scim_v2

        Create a new User
        """
        pass

    def test_users_delete_object_scim_v2(self) -> None:
        """Test case for users_delete_object_scim_v2

        Delete an existing User
        """
        pass

    def test_users_edit_object_scim_v2(self) -> None:
        """Test case for users_edit_object_scim_v2

        Edit an existing User
        """
        pass

    def test_users_get_list_scim_v2(self) -> None:
        """Test case for users_get_list_scim_v2

        Retrieve User list
        """
        pass

    def test_users_get_object_scim_v2(self) -> None:
        """Test case for users_get_object_scim_v2

        Retrieve an existing User
        """
        pass


if __name__ == '__main__':
    unittest.main()
