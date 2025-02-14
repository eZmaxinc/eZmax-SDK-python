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

from eZmaxApi.models.ezsigndocument_create_ezsignelements_positioned_by_word_v1_response_m_payload import EzsigndocumentCreateEzsignelementsPositionedByWordV1ResponseMPayload

class TestEzsigndocumentCreateEzsignelementsPositionedByWordV1ResponseMPayload(unittest.TestCase):
    """EzsigndocumentCreateEzsignelementsPositionedByWordV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentCreateEzsignelementsPositionedByWordV1ResponseMPayload:
        """Test EzsigndocumentCreateEzsignelementsPositionedByWordV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentCreateEzsignelementsPositionedByWordV1ResponseMPayload`
        """
        model = EzsigndocumentCreateEzsignelementsPositionedByWordV1ResponseMPayload()
        if include_optional:
            return EzsigndocumentCreateEzsignelementsPositionedByWordV1ResponseMPayload(
                a_pki_ezsignsignature_id = [
                    49
                    ],
                a_pki_ezsignformfieldgroup_id = [
                    26
                    ]
            )
        else:
            return EzsigndocumentCreateEzsignelementsPositionedByWordV1ResponseMPayload(
                a_pki_ezsignsignature_id = [
                    49
                    ],
                a_pki_ezsignformfieldgroup_id = [
                    26
                    ],
        )
        """

    def testEzsigndocumentCreateEzsignelementsPositionedByWordV1ResponseMPayload(self):
        """Test EzsigndocumentCreateEzsignelementsPositionedByWordV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
