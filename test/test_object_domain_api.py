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

from eZmaxApi.api.object_domain_api import ObjectDomainApi


class TestObjectDomainApi(unittest.TestCase):
    """ObjectDomainApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectDomainApi()

    def tearDown(self) -> None:
        pass

    def test_domain_create_object_v1(self) -> None:
        """Test case for domain_create_object_v1

        Create a new Domain
        """
        pass

    def test_domain_delete_object_v1(self) -> None:
        """Test case for domain_delete_object_v1

        Delete an existing Domain
        """
        pass

    def test_domain_get_list_v1(self) -> None:
        """Test case for domain_get_list_v1

        Retrieve Domain list
        """
        pass

    def test_domain_get_object_v2(self) -> None:
        """Test case for domain_get_object_v2

        Retrieve an existing Domain
        """
        pass


if __name__ == '__main__':
    unittest.main()
