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

from eZmaxApi.models.websocket_response_get_websocket_idv1 import WebsocketResponseGetWebsocketIDV1

class TestWebsocketResponseGetWebsocketIDV1(unittest.TestCase):
    """WebsocketResponseGetWebsocketIDV1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebsocketResponseGetWebsocketIDV1:
        """Test WebsocketResponseGetWebsocketIDV1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebsocketResponseGetWebsocketIDV1`
        """
        model = WebsocketResponseGetWebsocketIDV1()
        if include_optional:
            return WebsocketResponseGetWebsocketIDV1(
                e_websocket_messagetype = 'Response-GetWebsocketID-V1',
                m_payload = eZmaxApi.models.websocket_response_get_websocket_id_v1_m_payload.Websocket-Response-GetWebsocketID-V1-mPayload(
                    s_websocket_id = 'G_omidyY4osCFEQ=', )
            )
        else:
            return WebsocketResponseGetWebsocketIDV1(
                e_websocket_messagetype = 'Response-GetWebsocketID-V1',
                m_payload = eZmaxApi.models.websocket_response_get_websocket_id_v1_m_payload.Websocket-Response-GetWebsocketID-V1-mPayload(
                    s_websocket_id = 'G_omidyY4osCFEQ=', ),
        )
        """

    def testWebsocketResponseGetWebsocketIDV1(self):
        """Test WebsocketResponseGetWebsocketIDV1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
