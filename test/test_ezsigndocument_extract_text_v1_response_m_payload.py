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

from eZmaxApi.models.ezsigndocument_extract_text_v1_response_m_payload import EzsigndocumentExtractTextV1ResponseMPayload

class TestEzsigndocumentExtractTextV1ResponseMPayload(unittest.TestCase):
    """EzsigndocumentExtractTextV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentExtractTextV1ResponseMPayload:
        """Test EzsigndocumentExtractTextV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentExtractTextV1ResponseMPayload`
        """
        model = EzsigndocumentExtractTextV1ResponseMPayload()
        if include_optional:
            return EzsigndocumentExtractTextV1ResponseMPayload(
                s_text = 'Text extract from document'
            )
        else:
            return EzsigndocumentExtractTextV1ResponseMPayload(
                s_text = 'Text extract from document',
        )
        """

    def testEzsigndocumentExtractTextV1ResponseMPayload(self):
        """Test EzsigndocumentExtractTextV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
