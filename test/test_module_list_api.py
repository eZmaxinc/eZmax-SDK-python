"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.4
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.module_list_api import ModuleListApi  # noqa: E501


class TestModuleListApi(unittest.TestCase):
    """ModuleListApi unit test stubs"""

    def setUp(self):
        self.api = ModuleListApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_get_listpresentation_v1(self):
        """Test case for list_get_listpresentation_v1

        Get all Listpresentation for a specific list  # noqa: E501
        """
        pass

    def test_list_save_listpresentation_v1(self):
        """Test case for list_save_listpresentation_v1

        Save all Listpresentation for a specific list  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
