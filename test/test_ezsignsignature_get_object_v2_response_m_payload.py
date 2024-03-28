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

from eZmaxApi.models.ezsignsignature_get_object_v2_response_m_payload import EzsignsignatureGetObjectV2ResponseMPayload

class TestEzsignsignatureGetObjectV2ResponseMPayload(unittest.TestCase):
    """EzsignsignatureGetObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignatureGetObjectV2ResponseMPayload:
        """Test EzsignsignatureGetObjectV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignatureGetObjectV2ResponseMPayload`
        """
        model = EzsignsignatureGetObjectV2ResponseMPayload()
        if include_optional:
            return EzsignsignatureGetObjectV2ResponseMPayload(
                obj_ezsignsignature = eZmaxApi.models.ezsignsignature_response_compound.ezsignsignature-ResponseCompound()
            )
        else:
            return EzsignsignatureGetObjectV2ResponseMPayload(
                obj_ezsignsignature = eZmaxApi.models.ezsignsignature_response_compound.ezsignsignature-ResponseCompound(),
        )
        """

    def testEzsignsignatureGetObjectV2ResponseMPayload(self):
        """Test EzsignsignatureGetObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
