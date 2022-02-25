"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.5
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.module_authenticate_api import ModuleAuthenticateApi  # noqa: E501


class TestModuleAuthenticateApi(unittest.TestCase):
    """ModuleAuthenticateApi unit test stubs"""

    def setUp(self):
        self.api = ModuleAuthenticateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_authenticate_authenticate_v2(self):
        """Test case for authenticate_authenticate_v2

        Authenticate a user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
