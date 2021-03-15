"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.33
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api.module_user_api import ModuleUserApi  # noqa: E501


class TestModuleUserApi(unittest.TestCase):
    """ModuleUserApi unit test stubs"""

    def setUp(self):
        self.api = ModuleUserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_user_create_ezsignuser_v1(self):
        """Test case for user_create_ezsignuser_v1

        Create a new User of type Ezsignuser  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
