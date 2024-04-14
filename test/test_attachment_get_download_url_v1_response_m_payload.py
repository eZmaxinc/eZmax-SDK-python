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

from eZmaxApi.models.attachment_get_download_url_v1_response_m_payload import AttachmentGetDownloadUrlV1ResponseMPayload

class TestAttachmentGetDownloadUrlV1ResponseMPayload(unittest.TestCase):
    """AttachmentGetDownloadUrlV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttachmentGetDownloadUrlV1ResponseMPayload:
        """Test AttachmentGetDownloadUrlV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttachmentGetDownloadUrlV1ResponseMPayload`
        """
        model = AttachmentGetDownloadUrlV1ResponseMPayload()
        if include_optional:
            return AttachmentGetDownloadUrlV1ResponseMPayload(
                s_download_url = 'http://www.example.com/document.pdf'
            )
        else:
            return AttachmentGetDownloadUrlV1ResponseMPayload(
                s_download_url = 'http://www.example.com/document.pdf',
        )
        """

    def testAttachmentGetDownloadUrlV1ResponseMPayload(self):
        """Test AttachmentGetDownloadUrlV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
