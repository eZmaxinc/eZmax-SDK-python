"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.6
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.attempt_response_compound import AttemptResponseCompound
from eZmaxApi.model.webhook_response import WebhookResponse
globals()['AttemptResponseCompound'] = AttemptResponseCompound
globals()['WebhookResponse'] = WebhookResponse
from eZmaxApi.model.common_webhook import CommonWebhook


class TestCommonWebhook(unittest.TestCase):
    """CommonWebhook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCommonWebhook(self):
        """Test CommonWebhook"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CommonWebhook()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
