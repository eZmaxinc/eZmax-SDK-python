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

from eZmaxApi.api.scim_groups_api import ScimGroupsApi


class TestScimGroupsApi(unittest.TestCase):
    """ScimGroupsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ScimGroupsApi()

    def tearDown(self) -> None:
        pass

    def test_groups_create_object_scim_v2(self) -> None:
        """Test case for groups_create_object_scim_v2

        Create a new Usergroup
        """
        pass

    def test_groups_delete_object_scim_v2(self) -> None:
        """Test case for groups_delete_object_scim_v2

        Delete an existing Usergroup
        """
        pass

    def test_groups_edit_object_scim_v2(self) -> None:
        """Test case for groups_edit_object_scim_v2

        Edit an existing Usergroup
        """
        pass

    def test_groups_get_list_scim_v2(self) -> None:
        """Test case for groups_get_list_scim_v2

        Retrieve Usergroup list
        """
        pass

    def test_groups_get_object_scim_v2(self) -> None:
        """Test case for groups_get_object_scim_v2

        Retrieve an existing Usergroup
        """
        pass


if __name__ == '__main__':
    unittest.main()
