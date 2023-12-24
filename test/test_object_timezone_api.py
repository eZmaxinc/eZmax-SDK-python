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

from eZmaxApi.api.object_timezone_api import ObjectTimezoneApi


class TestObjectTimezoneApi(unittest.TestCase):
    """ObjectTimezoneApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectTimezoneApi()

    def tearDown(self) -> None:
        pass

    def test_timezone_get_autocomplete_v2(self) -> None:
        """Test case for timezone_get_autocomplete_v2

        Retrieve Timezones and IDs
        """
        pass


if __name__ == '__main__':
    unittest.main()
