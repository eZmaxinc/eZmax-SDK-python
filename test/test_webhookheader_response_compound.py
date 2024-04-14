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

from eZmaxApi.models.webhookheader_response_compound import WebhookheaderResponseCompound

class TestWebhookheaderResponseCompound(unittest.TestCase):
    """WebhookheaderResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookheaderResponseCompound:
        """Test WebhookheaderResponseCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookheaderResponseCompound`
        """
        model = WebhookheaderResponseCompound()
        if include_optional:
            return WebhookheaderResponseCompound(
                pki_webhookheader_id = 77,
                fki_webhook_id = 77,
                s_webhookheader_name = 'Authorization',
                s_webhookheader_value = 'd75fca0e12b6c671e7f6d4df0cf59e4e'
            )
        else:
            return WebhookheaderResponseCompound(
                pki_webhookheader_id = 77,
                fki_webhook_id = 77,
                s_webhookheader_name = 'Authorization',
                s_webhookheader_value = 'd75fca0e12b6c671e7f6d4df0cf59e4e',
        )
        """

    def testWebhookheaderResponseCompound(self):
        """Test WebhookheaderResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
