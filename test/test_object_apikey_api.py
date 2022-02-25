"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.5
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.object_apikey_api import ObjectApikeyApi  # noqa: E501


class TestObjectApikeyApi(unittest.TestCase):
    """ObjectApikeyApi unit test stubs"""

    def setUp(self):
        self.api = ObjectApikeyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_apikey_create_object_v1(self):
        """Test case for apikey_create_object_v1

        Create a new Apikey  # noqa: E501
        """
        pass

    def test_apikey_create_object_v2(self):
        """Test case for apikey_create_object_v2

        Create a new Apikey  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
