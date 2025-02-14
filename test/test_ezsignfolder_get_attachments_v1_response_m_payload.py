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

from eZmaxApi.models.ezsignfolder_get_attachments_v1_response_m_payload import EzsignfolderGetAttachmentsV1ResponseMPayload

class TestEzsignfolderGetAttachmentsV1ResponseMPayload(unittest.TestCase):
    """EzsignfolderGetAttachmentsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfolderGetAttachmentsV1ResponseMPayload:
        """Test EzsignfolderGetAttachmentsV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfolderGetAttachmentsV1ResponseMPayload`
        """
        model = EzsignfolderGetAttachmentsV1ResponseMPayload()
        if include_optional:
            return EzsignfolderGetAttachmentsV1ResponseMPayload(
                a_obj_attachmentdocumenttype = [
                    eZmaxApi.models.custom_attachmentdocumenttype_response.Custom-Attachmentdocumenttype-Response(
                        e_attachment_documenttype = 'Adjustment', 
                        a_obj_attachment = [
                            eZmaxApi.models.custom_attachment_response.Custom-Attachment-Response()
                            ], )
                    ]
            )
        else:
            return EzsignfolderGetAttachmentsV1ResponseMPayload(
                a_obj_attachmentdocumenttype = [
                    eZmaxApi.models.custom_attachmentdocumenttype_response.Custom-Attachmentdocumenttype-Response(
                        e_attachment_documenttype = 'Adjustment', 
                        a_obj_attachment = [
                            eZmaxApi.models.custom_attachment_response.Custom-Attachment-Response()
                            ], )
                    ],
        )
        """

    def testEzsignfolderGetAttachmentsV1ResponseMPayload(self):
        """Test EzsignfolderGetAttachmentsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
