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

from eZmaxApi.api.object_country_api import ObjectCountryApi


class TestObjectCountryApi(unittest.TestCase):
    """ObjectCountryApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectCountryApi()

    def tearDown(self) -> None:
        pass

    def test_country_get_autocomplete_v2(self) -> None:
        """Test case for country_get_autocomplete_v2

        Retrieve Countries and IDs
        """
        pass


if __name__ == '__main__':
    unittest.main()
