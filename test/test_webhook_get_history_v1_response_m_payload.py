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

from eZmaxApi.models.webhook_get_history_v1_response_m_payload import WebhookGetHistoryV1ResponseMPayload

class TestWebhookGetHistoryV1ResponseMPayload(unittest.TestCase):
    """WebhookGetHistoryV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookGetHistoryV1ResponseMPayload:
        """Test WebhookGetHistoryV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookGetHistoryV1ResponseMPayload`
        """
        model = WebhookGetHistoryV1ResponseMPayload()
        if include_optional:
            return WebhookGetHistoryV1ResponseMPayload(
                a_obj_webhooklog = [
                    eZmaxApi.models.custom_webhooklog_response.Custom-Webhooklog-Response()
                    ]
            )
        else:
            return WebhookGetHistoryV1ResponseMPayload(
                a_obj_webhooklog = [
                    eZmaxApi.models.custom_webhooklog_response.Custom-Webhooklog-Response()
                    ],
        )
        """

    def testWebhookGetHistoryV1ResponseMPayload(self):
        """Test WebhookGetHistoryV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
