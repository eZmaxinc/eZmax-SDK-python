"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.13
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.object_franchiseoffice_api import ObjectFranchiseofficeApi  # noqa: E501


class TestObjectFranchiseofficeApi(unittest.TestCase):
    """ObjectFranchiseofficeApi unit test stubs"""

    def setUp(self):
        self.api = ObjectFranchiseofficeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_franchiseoffice_get_autocomplete_v1(self):
        """Test case for franchiseoffice_get_autocomplete_v1

        Retrieve Franchiseoffices and IDs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
