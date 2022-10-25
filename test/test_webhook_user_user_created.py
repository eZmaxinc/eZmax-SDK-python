"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.11
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.attempt_response_compound import AttemptResponseCompound
from eZmaxApi.model.common_webhook import CommonWebhook
from eZmaxApi.model.custom_webhook_response import CustomWebhookResponse
from eZmaxApi.model.user_response_compound import UserResponseCompound
from eZmaxApi.model.webhook_user_user_created_all_of import WebhookUserUserCreatedAllOf
globals()['AttemptResponseCompound'] = AttemptResponseCompound
globals()['CommonWebhook'] = CommonWebhook
globals()['CustomWebhookResponse'] = CustomWebhookResponse
globals()['UserResponseCompound'] = UserResponseCompound
globals()['WebhookUserUserCreatedAllOf'] = WebhookUserUserCreatedAllOf
from eZmaxApi.model.webhook_user_user_created import WebhookUserUserCreated


class TestWebhookUserUserCreated(unittest.TestCase):
    """WebhookUserUserCreated unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWebhookUserUserCreated(self):
        """Test WebhookUserUserCreated"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WebhookUserUserCreated()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
