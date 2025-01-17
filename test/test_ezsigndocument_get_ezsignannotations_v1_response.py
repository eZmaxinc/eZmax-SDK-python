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

from eZmaxApi.models.ezsigndocument_get_ezsignannotations_v1_response import EzsigndocumentGetEzsignannotationsV1Response

class TestEzsigndocumentGetEzsignannotationsV1Response(unittest.TestCase):
    """EzsigndocumentGetEzsignannotationsV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentGetEzsignannotationsV1Response:
        """Test EzsigndocumentGetEzsignannotationsV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentGetEzsignannotationsV1Response`
        """
        model = EzsigndocumentGetEzsignannotationsV1Response()
        if include_optional:
            return EzsigndocumentGetEzsignannotationsV1Response(
                m_payload = eZmaxApi.models.ezsigndocument_get_ezsignannotations_v1_response_m_payload.ezsigndocument-getEzsignannotations-v1-Response-mPayload(
                    a_obj_ezsignannotation = [
                        eZmaxApi.models.ezsignannotation_response_compound.ezsignannotation-ResponseCompound()
                        ], )
            )
        else:
            return EzsigndocumentGetEzsignannotationsV1Response(
                m_payload = eZmaxApi.models.ezsigndocument_get_ezsignannotations_v1_response_m_payload.ezsigndocument-getEzsignannotations-v1-Response-mPayload(
                    a_obj_ezsignannotation = [
                        eZmaxApi.models.ezsignannotation_response_compound.ezsignannotation-ResponseCompound()
                        ], ),
        )
        """

    def testEzsigndocumentGetEzsignannotationsV1Response(self):
        """Test EzsigndocumentGetEzsignannotationsV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
