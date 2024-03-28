# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.0
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from eZmaxApi.models.custom_attachmentdocumenttype_response import CustomAttachmentdocumenttypeResponse

class TestCustomAttachmentdocumenttypeResponse(unittest.TestCase):
    """CustomAttachmentdocumenttypeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomAttachmentdocumenttypeResponse:
        """Test CustomAttachmentdocumenttypeResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomAttachmentdocumenttypeResponse`
        """
        model = CustomAttachmentdocumenttypeResponse()
        if include_optional:
            return CustomAttachmentdocumenttypeResponse(
                e_attachment_documenttype = 'Adjustment',
                a_obj_attachment = [
                    eZmaxApi.models.custom_attachment_response.Custom-Attachment-Response()
                    ]
            )
        else:
            return CustomAttachmentdocumenttypeResponse(
                e_attachment_documenttype = 'Adjustment',
                a_obj_attachment = [
                    eZmaxApi.models.custom_attachment_response.Custom-Attachment-Response()
                    ],
        )
        """

    def testCustomAttachmentdocumenttypeResponse(self):
        """Test CustomAttachmentdocumenttypeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
