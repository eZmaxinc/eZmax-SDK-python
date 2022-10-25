"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.11
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.object_timezone_api import ObjectTimezoneApi  # noqa: E501


class TestObjectTimezoneApi(unittest.TestCase):
    """ObjectTimezoneApi unit test stubs"""

    def setUp(self):
        self.api = ObjectTimezoneApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_timezone_get_autocomplete_v1(self):
        """Test case for timezone_get_autocomplete_v1

        Retrieve Timezones and IDs  # noqa: E501
        """
        pass

    def test_timezone_get_autocomplete_v2(self):
        """Test case for timezone_get_autocomplete_v2

        Retrieve Timezones and IDs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
