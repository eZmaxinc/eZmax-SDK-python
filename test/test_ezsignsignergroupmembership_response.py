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

from eZmaxApi.models.ezsignsignergroupmembership_response import EzsignsignergroupmembershipResponse

class TestEzsignsignergroupmembershipResponse(unittest.TestCase):
    """EzsignsignergroupmembershipResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignergroupmembershipResponse:
        """Test EzsignsignergroupmembershipResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignergroupmembershipResponse`
        """
        model = EzsignsignergroupmembershipResponse()
        if include_optional:
            return EzsignsignergroupmembershipResponse(
                pki_ezsignsignergroupmembership_id = 153,
                fki_ezsignsignergroup_id = 27,
                fki_ezsignsigner_id = 89,
                fki_user_id = 70,
                fki_usergroup_id = 2
            )
        else:
            return EzsignsignergroupmembershipResponse(
                pki_ezsignsignergroupmembership_id = 153,
                fki_ezsignsignergroup_id = 27,
        )
        """

    def testEzsignsignergroupmembershipResponse(self):
        """Test EzsignsignergroupmembershipResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
