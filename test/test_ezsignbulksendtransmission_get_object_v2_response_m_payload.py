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

from eZmaxApi.models.ezsignbulksendtransmission_get_object_v2_response_m_payload import EzsignbulksendtransmissionGetObjectV2ResponseMPayload  # noqa: E501

class TestEzsignbulksendtransmissionGetObjectV2ResponseMPayload(unittest.TestCase):
    """EzsignbulksendtransmissionGetObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignbulksendtransmissionGetObjectV2ResponseMPayload:
        """Test EzsignbulksendtransmissionGetObjectV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignbulksendtransmissionGetObjectV2ResponseMPayload`
        """
        model = EzsignbulksendtransmissionGetObjectV2ResponseMPayload()  # noqa: E501
        if include_optional:
            return EzsignbulksendtransmissionGetObjectV2ResponseMPayload(
                obj_ezsignbulksendtransmission = eZmaxApi.models.ezsignbulksendtransmission_response_compound.ezsignbulksendtransmission-ResponseCompound()
            )
        else:
            return EzsignbulksendtransmissionGetObjectV2ResponseMPayload(
                obj_ezsignbulksendtransmission = eZmaxApi.models.ezsignbulksendtransmission_response_compound.ezsignbulksendtransmission-ResponseCompound(),
        )
        """

    def testEzsignbulksendtransmissionGetObjectV2ResponseMPayload(self):
        """Test EzsignbulksendtransmissionGetObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
