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

from eZmaxApi.models.attachment_get_attachmentlogs_v1_response_m_payload import AttachmentGetAttachmentlogsV1ResponseMPayload

class TestAttachmentGetAttachmentlogsV1ResponseMPayload(unittest.TestCase):
    """AttachmentGetAttachmentlogsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttachmentGetAttachmentlogsV1ResponseMPayload:
        """Test AttachmentGetAttachmentlogsV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttachmentGetAttachmentlogsV1ResponseMPayload`
        """
        model = AttachmentGetAttachmentlogsV1ResponseMPayload()
        if include_optional:
            return AttachmentGetAttachmentlogsV1ResponseMPayload(
                a_obj_attachmentlog = [
                    eZmaxApi.models.attachmentlog_response_compound.attachmentlog-ResponseCompound()
                    ]
            )
        else:
            return AttachmentGetAttachmentlogsV1ResponseMPayload(
                a_obj_attachmentlog = [
                    eZmaxApi.models.attachmentlog_response_compound.attachmentlog-ResponseCompound()
                    ],
        )
        """

    def testAttachmentGetAttachmentlogsV1ResponseMPayload(self):
        """Test AttachmentGetAttachmentlogsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
