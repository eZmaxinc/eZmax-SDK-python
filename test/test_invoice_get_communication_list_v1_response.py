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
import datetime

from eZmaxApi.models.invoice_get_communication_list_v1_response import InvoiceGetCommunicationListV1Response  # noqa: E501

class TestInvoiceGetCommunicationListV1Response(unittest.TestCase):
    """InvoiceGetCommunicationListV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceGetCommunicationListV1Response:
        """Test InvoiceGetCommunicationListV1Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceGetCommunicationListV1Response`
        """
        model = InvoiceGetCommunicationListV1Response()  # noqa: E501
        if include_optional:
            return InvoiceGetCommunicationListV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload_get_list.Common-Response-objDebugPayload_getList(),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.invoice_get_communication_list_v1_response_m_payload.invoice-getCommunicationList-v1-Response-mPayload()
            )
        else:
            return InvoiceGetCommunicationListV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload_get_list.Common-Response-objDebugPayload_getList(),
                m_payload = eZmaxApi.models.invoice_get_communication_list_v1_response_m_payload.invoice-getCommunicationList-v1-Response-mPayload(),
        )
        """

    def testInvoiceGetCommunicationListV1Response(self):
        """Test InvoiceGetCommunicationListV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
