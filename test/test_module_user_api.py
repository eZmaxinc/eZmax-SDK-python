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

from eZmaxApi.api.module_user_api import ModuleUserApi


class TestModuleUserApi(unittest.TestCase):
    """ModuleUserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ModuleUserApi()

    def tearDown(self) -> None:
        pass

    def test_user_create_ezsignuser_v1(self) -> None:
        """Test case for user_create_ezsignuser_v1

        Create a new User of type Ezsignuser
        """
        pass


if __name__ == '__main__':
    unittest.main()
