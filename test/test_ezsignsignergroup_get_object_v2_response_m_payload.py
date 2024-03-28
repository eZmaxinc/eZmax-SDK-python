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

from eZmaxApi.models.ezsignsignergroup_get_object_v2_response_m_payload import EzsignsignergroupGetObjectV2ResponseMPayload

class TestEzsignsignergroupGetObjectV2ResponseMPayload(unittest.TestCase):
    """EzsignsignergroupGetObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignergroupGetObjectV2ResponseMPayload:
        """Test EzsignsignergroupGetObjectV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignergroupGetObjectV2ResponseMPayload`
        """
        model = EzsignsignergroupGetObjectV2ResponseMPayload()
        if include_optional:
            return EzsignsignergroupGetObjectV2ResponseMPayload(
                obj_ezsignsignergroup = eZmaxApi.models.ezsignsignergroup_response_compound.ezsignsignergroup-ResponseCompound()
            )
        else:
            return EzsignsignergroupGetObjectV2ResponseMPayload(
                obj_ezsignsignergroup = eZmaxApi.models.ezsignsignergroup_response_compound.ezsignsignergroup-ResponseCompound(),
        )
        """

    def testEzsignsignergroupGetObjectV2ResponseMPayload(self):
        """Test EzsignsignergroupGetObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
