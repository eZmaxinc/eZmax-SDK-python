"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.38
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.object_franchisebroker_api import ObjectFranchisebrokerApi  # noqa: E501


class TestObjectFranchisebrokerApi(unittest.TestCase):
    """ObjectFranchisebrokerApi unit test stubs"""

    def setUp(self):
        self.api = ObjectFranchisebrokerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_franchisebroker_get_autocomplete_v1(self):
        """Test case for franchisebroker_get_autocomplete_v1

        Retrieve Franchisebrokers and IDs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
