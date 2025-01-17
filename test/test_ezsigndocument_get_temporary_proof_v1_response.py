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

from eZmaxApi.models.ezsigndocument_get_temporary_proof_v1_response import EzsigndocumentGetTemporaryProofV1Response

class TestEzsigndocumentGetTemporaryProofV1Response(unittest.TestCase):
    """EzsigndocumentGetTemporaryProofV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentGetTemporaryProofV1Response:
        """Test EzsigndocumentGetTemporaryProofV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentGetTemporaryProofV1Response`
        """
        model = EzsigndocumentGetTemporaryProofV1Response()
        if include_optional:
            return EzsigndocumentGetTemporaryProofV1Response(
                m_payload = eZmaxApi.models.ezsigndocument_get_temporary_proof_v1_response_m_payload.ezsigndocument-getTemporaryProof-v1-Response-mPayload(
                    a_obj_ezsigndocumentlog = [
                        eZmaxApi.models.ezsigndocumentlog_response_compound.ezsigndocumentlog-ResponseCompound()
                        ], )
            )
        else:
            return EzsigndocumentGetTemporaryProofV1Response(
                m_payload = eZmaxApi.models.ezsigndocument_get_temporary_proof_v1_response_m_payload.ezsigndocument-getTemporaryProof-v1-Response-mPayload(
                    a_obj_ezsigndocumentlog = [
                        eZmaxApi.models.ezsigndocumentlog_response_compound.ezsigndocumentlog-ResponseCompound()
                        ], ),
        )
        """

    def testEzsigndocumentGetTemporaryProofV1Response(self):
        """Test EzsigndocumentGetTemporaryProofV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
