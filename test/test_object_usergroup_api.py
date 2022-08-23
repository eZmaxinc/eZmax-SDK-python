"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.10
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.object_usergroup_api import ObjectUsergroupApi  # noqa: E501


class TestObjectUsergroupApi(unittest.TestCase):
    """ObjectUsergroupApi unit test stubs"""

    def setUp(self):
        self.api = ObjectUsergroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_usergroup_get_autocomplete_v1(self):
        """Test case for usergroup_get_autocomplete_v1

        Retrieve Usergroups and IDs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
