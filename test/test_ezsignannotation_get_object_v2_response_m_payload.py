# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.1
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from eZmaxApi.models.ezsignannotation_get_object_v2_response_m_payload import EzsignannotationGetObjectV2ResponseMPayload

class TestEzsignannotationGetObjectV2ResponseMPayload(unittest.TestCase):
    """EzsignannotationGetObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignannotationGetObjectV2ResponseMPayload:
        """Test EzsignannotationGetObjectV2ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignannotationGetObjectV2ResponseMPayload`
        """
        model = EzsignannotationGetObjectV2ResponseMPayload()
        if include_optional:
            return EzsignannotationGetObjectV2ResponseMPayload(
                obj_ezsignannotation = eZmaxApi.models.ezsignannotation_response_compound.ezsignannotation-ResponseCompound()
            )
        else:
            return EzsignannotationGetObjectV2ResponseMPayload(
                obj_ezsignannotation = eZmaxApi.models.ezsignannotation_response_compound.ezsignannotation-ResponseCompound(),
        )
        """

    def testEzsignannotationGetObjectV2ResponseMPayload(self):
        """Test EzsignannotationGetObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
