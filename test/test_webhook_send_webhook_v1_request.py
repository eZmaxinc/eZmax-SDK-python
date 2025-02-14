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

from eZmaxApi.models.webhook_send_webhook_v1_request import WebhookSendWebhookV1Request

class TestWebhookSendWebhookV1Request(unittest.TestCase):
    """WebhookSendWebhookV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookSendWebhookV1Request:
        """Test WebhookSendWebhookV1Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookSendWebhookV1Request`
        """
        model = WebhookSendWebhookV1Request()
        if include_optional:
            return WebhookSendWebhookV1Request(
                e_webhook_module = 'Ezsign',
                e_webhook_ezsignevent = 'FolderCompleted',
                e_webhook_managementevent = 'UserCreated',
                fki_ezsignfolder_id = 33,
                fki_ezsigndocument_id = 97,
                fki_ezsignsigner_id = 89,
                fki_user_id = 70,
                fki_userstaged_id = 90
            )
        else:
            return WebhookSendWebhookV1Request(
                e_webhook_module = 'Ezsign',
        )
        """

    def testWebhookSendWebhookV1Request(self):
        """Test WebhookSendWebhookV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
