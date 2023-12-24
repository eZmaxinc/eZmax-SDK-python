# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.0
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from eZmaxApi.models.permission_request_compound import PermissionRequestCompound

class TestPermissionRequestCompound(unittest.TestCase):
    """PermissionRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PermissionRequestCompound:
        """Test PermissionRequestCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PermissionRequestCompound`
        """
        model = PermissionRequestCompound()
        if include_optional:
            return PermissionRequestCompound(
                pki_permission_id = 31,
                fki_user_id = 70,
                fki_apikey_id = 99,
                fki_usergroup_id = 2,
                fki_company_id = 1,
                fki_modulesection_id = 53
            )
        else:
            return PermissionRequestCompound(
                fki_modulesection_id = 53,
        )
        """

    def testPermissionRequestCompound(self):
        """Test PermissionRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
