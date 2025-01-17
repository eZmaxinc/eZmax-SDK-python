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

from eZmaxApi.models.ezsigndocument_extract_text_v1_response import EzsigndocumentExtractTextV1Response

class TestEzsigndocumentExtractTextV1Response(unittest.TestCase):
    """EzsigndocumentExtractTextV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentExtractTextV1Response:
        """Test EzsigndocumentExtractTextV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentExtractTextV1Response`
        """
        model = EzsigndocumentExtractTextV1Response()
        if include_optional:
            return EzsigndocumentExtractTextV1Response(
                m_payload = eZmaxApi.models.ezsigndocument_extract_text_v1_response_m_payload.ezsigndocument-extractText-v1-Response-mPayload(
                    s_text = 'Text extract from document', )
            )
        else:
            return EzsigndocumentExtractTextV1Response(
                m_payload = eZmaxApi.models.ezsigndocument_extract_text_v1_response_m_payload.ezsigndocument-extractText-v1-Response-mPayload(
                    s_text = 'Text extract from document', ),
        )
        """

    def testEzsigndocumentExtractTextV1Response(self):
        """Test EzsigndocumentExtractTextV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
