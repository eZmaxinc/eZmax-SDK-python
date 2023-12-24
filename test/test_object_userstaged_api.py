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

from eZmaxApi.api.object_userstaged_api import ObjectUserstagedApi


class TestObjectUserstagedApi(unittest.TestCase):
    """ObjectUserstagedApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectUserstagedApi()

    def tearDown(self) -> None:
        pass

    def test_userstaged_create_user_v1(self) -> None:
        """Test case for userstaged_create_user_v1

        Create a User from a Userstaged and then map it
        """
        pass

    def test_userstaged_delete_object_v1(self) -> None:
        """Test case for userstaged_delete_object_v1

        Delete an existing Userstaged
        """
        pass

    def test_userstaged_get_list_v1(self) -> None:
        """Test case for userstaged_get_list_v1

        Retrieve Userstaged list
        """
        pass

    def test_userstaged_get_object_v2(self) -> None:
        """Test case for userstaged_get_object_v2

        Retrieve an existing Userstaged
        """
        pass

    def test_userstaged_map_v1(self) -> None:
        """Test case for userstaged_map_v1

        Map the Userstaged to an existing user
        """
        pass


if __name__ == '__main__':
    unittest.main()
