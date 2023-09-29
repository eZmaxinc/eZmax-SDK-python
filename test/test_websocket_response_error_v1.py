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

from eZmaxApi.models.websocket_response_error_v1 import WebsocketResponseErrorV1  # noqa: E501

class TestWebsocketResponseErrorV1(unittest.TestCase):
    """WebsocketResponseErrorV1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebsocketResponseErrorV1:
        """Test WebsocketResponseErrorV1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebsocketResponseErrorV1`
        """
        model = WebsocketResponseErrorV1()  # noqa: E501
        if include_optional:
            return WebsocketResponseErrorV1(
                e_websocket_messagetype = 'Response-Error-V1',
                m_payload = eZmaxApi.models.websocket_response_error_v1_m_payload.Websocket-Response-Error-V1-mPayload(
                    s_error_message = 'Invalid Signature Headers', 
                    e_error_code = 'BADREQUEST', )
            )
        else:
            return WebsocketResponseErrorV1(
                e_websocket_messagetype = 'Response-Error-V1',
                m_payload = eZmaxApi.models.websocket_response_error_v1_m_payload.Websocket-Response-Error-V1-mPayload(
                    s_error_message = 'Invalid Signature Headers', 
                    e_error_code = 'BADREQUEST', ),
        )
        """

    def testWebsocketResponseErrorV1(self):
        """Test WebsocketResponseErrorV1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()