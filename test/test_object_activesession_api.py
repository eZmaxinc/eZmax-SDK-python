"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.5
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.object_activesession_api import ObjectActivesessionApi  # noqa: E501


class TestObjectActivesessionApi(unittest.TestCase):
    """ObjectActivesessionApi unit test stubs"""

    def setUp(self):
        self.api = ObjectActivesessionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activesession_get_current_v1(self):
        """Test case for activesession_get_current_v1

        Get Current Activesession  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
