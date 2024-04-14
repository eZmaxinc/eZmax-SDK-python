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

from eZmaxApi.models.webhookheader_request import WebhookheaderRequest

class TestWebhookheaderRequest(unittest.TestCase):
    """WebhookheaderRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookheaderRequest:
        """Test WebhookheaderRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookheaderRequest`
        """
        model = WebhookheaderRequest()
        if include_optional:
            return WebhookheaderRequest(
                pki_webhookheader_id = 77,
                s_webhookheader_name = 'Authorization',
                s_webhookheader_value = 'd75fca0e12b6c671e7f6d4df0cf59e4e'
            )
        else:
            return WebhookheaderRequest(
                s_webhookheader_name = 'Authorization',
                s_webhookheader_value = 'd75fca0e12b6c671e7f6d4df0cf59e4e',
        )
        """

    def testWebhookheaderRequest(self):
        """Test WebhookheaderRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()