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

from eZmaxApi.models.ezsigndocument_get_ezsignsignatures_v1_response import EzsigndocumentGetEzsignsignaturesV1Response

class TestEzsigndocumentGetEzsignsignaturesV1Response(unittest.TestCase):
    """EzsigndocumentGetEzsignsignaturesV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentGetEzsignsignaturesV1Response:
        """Test EzsigndocumentGetEzsignsignaturesV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentGetEzsignsignaturesV1Response`
        """
        model = EzsigndocumentGetEzsignsignaturesV1Response()
        if include_optional:
            return EzsigndocumentGetEzsignsignaturesV1Response(
                m_payload = eZmaxApi.models.ezsigndocument_get_ezsignsignatures_v1_response_m_payload.ezsigndocument-getEzsignsignatures-v1-Response-mPayload(
                    a_obj_ezsignsignature = [
                        eZmaxApi.models.ezsignsignature_response_compound.ezsignsignature-ResponseCompound()
                        ], )
            )
        else:
            return EzsigndocumentGetEzsignsignaturesV1Response(
                m_payload = eZmaxApi.models.ezsigndocument_get_ezsignsignatures_v1_response_m_payload.ezsigndocument-getEzsignsignatures-v1-Response-mPayload(
                    a_obj_ezsignsignature = [
                        eZmaxApi.models.ezsignsignature_response_compound.ezsignsignature-ResponseCompound()
                        ], ),
        )
        """

    def testEzsigndocumentGetEzsignsignaturesV1Response(self):
        """Test EzsigndocumentGetEzsignsignaturesV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
