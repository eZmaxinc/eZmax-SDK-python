"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.35
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.model.attempt_response import AttemptResponse
from eZmaxinc/eZmax-SDK-python.model.webhook_response import WebhookResponse
globals()['AttemptResponse'] = AttemptResponse
globals()['WebhookResponse'] = WebhookResponse
from eZmaxinc/eZmax-SDK-python.model.common_webhook import CommonWebhook


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
