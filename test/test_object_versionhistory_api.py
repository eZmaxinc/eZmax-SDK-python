"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.16
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.object_versionhistory_api import ObjectVersionhistoryApi  # noqa: E501


class TestObjectVersionhistoryApi(unittest.TestCase):
    """ObjectVersionhistoryApi unit test stubs"""

    def setUp(self):
        self.api = ObjectVersionhistoryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_versionhistory_get_object_v2(self):
        """Test case for versionhistory_get_object_v2

        Retrieve an existing Versionhistory  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
