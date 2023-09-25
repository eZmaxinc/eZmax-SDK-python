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

from eZmaxApi.models.ezsignsignergroup_get_ezsignsignergroupmemberships_v1_response_m_payload import EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload  # noqa: E501

class TestEzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload(unittest.TestCase):
    """EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload:
        """Test EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload`
        """
        model = EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload()  # noqa: E501
        if include_optional:
            return EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload(
                a_obj_ezsignsignergroupmembership = [
                    eZmaxApi.models.ezsignsignergroupmembership_response_compound.ezsignsignergroupmembership-ResponseCompound()
                    ]
            )
        else:
            return EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload(
                a_obj_ezsignsignergroupmembership = [
                    eZmaxApi.models.ezsignsignergroupmembership_response_compound.ezsignsignergroupmembership-ResponseCompound()
                    ],
        )
        """

    def testEzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload(self):
        """Test EzsignsignergroupGetEzsignsignergroupmembershipsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
