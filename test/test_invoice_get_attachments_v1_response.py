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

from eZmaxApi.models.invoice_get_attachments_v1_response import InvoiceGetAttachmentsV1Response

class TestInvoiceGetAttachmentsV1Response(unittest.TestCase):
    """InvoiceGetAttachmentsV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceGetAttachmentsV1Response:
        """Test InvoiceGetAttachmentsV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceGetAttachmentsV1Response`
        """
        model = InvoiceGetAttachmentsV1Response()
        if include_optional:
            return InvoiceGetAttachmentsV1Response(
                m_payload = eZmaxApi.models.invoice_get_attachments_v1_response_m_payload.invoice-getAttachments-v1-Response-mPayload(
                    a_obj_attachmentdocumenttype = [
                        eZmaxApi.models.custom_attachmentdocumenttype_response.Custom-Attachmentdocumenttype-Response(
                            e_attachment_documenttype = 'Adjustment', 
                            a_obj_attachment = [
                                eZmaxApi.models.custom_attachment_response.Custom-Attachment-Response()
                                ], )
                        ], )
            )
        else:
            return InvoiceGetAttachmentsV1Response(
                m_payload = eZmaxApi.models.invoice_get_attachments_v1_response_m_payload.invoice-getAttachments-v1-Response-mPayload(
                    a_obj_attachmentdocumenttype = [
                        eZmaxApi.models.custom_attachmentdocumenttype_response.Custom-Attachmentdocumenttype-Response(
                            e_attachment_documenttype = 'Adjustment', 
                            a_obj_attachment = [
                                eZmaxApi.models.custom_attachment_response.Custom-Attachment-Response()
                                ], )
                        ], ),
        )
        """

    def testInvoiceGetAttachmentsV1Response(self):
        """Test InvoiceGetAttachmentsV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
