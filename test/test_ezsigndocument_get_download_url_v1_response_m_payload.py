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

from eZmaxApi.models.ezsigndocument_get_download_url_v1_response_m_payload import EzsigndocumentGetDownloadUrlV1ResponseMPayload

class TestEzsigndocumentGetDownloadUrlV1ResponseMPayload(unittest.TestCase):
    """EzsigndocumentGetDownloadUrlV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentGetDownloadUrlV1ResponseMPayload:
        """Test EzsigndocumentGetDownloadUrlV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentGetDownloadUrlV1ResponseMPayload`
        """
        model = EzsigndocumentGetDownloadUrlV1ResponseMPayload()
        if include_optional:
            return EzsigndocumentGetDownloadUrlV1ResponseMPayload(
                s_download_url = 'http://www.example.com/document.pdf'
            )
        else:
            return EzsigndocumentGetDownloadUrlV1ResponseMPayload(
                s_download_url = 'http://www.example.com/document.pdf',
        )
        """

    def testEzsigndocumentGetDownloadUrlV1ResponseMPayload(self):
        """Test EzsigndocumentGetDownloadUrlV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
