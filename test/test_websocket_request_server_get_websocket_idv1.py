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

from eZmaxApi.models.websocket_request_server_get_websocket_idv1 import WebsocketRequestServerGetWebsocketIDV1

class TestWebsocketRequestServerGetWebsocketIDV1(unittest.TestCase):
    """WebsocketRequestServerGetWebsocketIDV1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebsocketRequestServerGetWebsocketIDV1:
        """Test WebsocketRequestServerGetWebsocketIDV1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebsocketRequestServerGetWebsocketIDV1`
        """
        model = WebsocketRequestServerGetWebsocketIDV1()
        if include_optional:
            return WebsocketRequestServerGetWebsocketIDV1(
                e_websocket_messagetype = 'RequestServer-GetWebsocketID-V1'
            )
        else:
            return WebsocketRequestServerGetWebsocketIDV1(
                e_websocket_messagetype = 'RequestServer-GetWebsocketID-V1',
        )
        """

    def testWebsocketRequestServerGetWebsocketIDV1(self):
        """Test WebsocketRequestServerGetWebsocketIDV1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
