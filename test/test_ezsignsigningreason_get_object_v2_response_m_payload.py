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

from eZmaxApi.models.ezsignsigningreason_get_object_v2_response_m_payload import EzsignsigningreasonGetObjectV2ResponseMPayload

class TestEzsignsigningreasonGetObjectV2ResponseMPayload(unittest.TestCase):
    """EzsignsigningreasonGetObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsigningreasonGetObjectV2ResponseMPayload:
        """Test EzsignsigningreasonGetObjectV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsigningreasonGetObjectV2ResponseMPayload`
        """
        model = EzsignsigningreasonGetObjectV2ResponseMPayload()
        if include_optional:
            return EzsignsigningreasonGetObjectV2ResponseMPayload(
                obj_ezsignsigningreason = eZmaxApi.models.ezsignsigningreason_response_compound.ezsignsigningreason-ResponseCompound()
            )
        else:
            return EzsignsigningreasonGetObjectV2ResponseMPayload(
                obj_ezsignsigningreason = eZmaxApi.models.ezsignsigningreason_response_compound.ezsignsigningreason-ResponseCompound(),
        )
        """

    def testEzsignsigningreasonGetObjectV2ResponseMPayload(self):
        """Test EzsignsigningreasonGetObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
