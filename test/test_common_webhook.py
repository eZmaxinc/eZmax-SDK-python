"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.16
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.attempt_response_compound import AttemptResponseCompound
from eZmaxApi.model.custom_webhook_response import CustomWebhookResponse
globals()['AttemptResponseCompound'] = AttemptResponseCompound
globals()['CustomWebhookResponse'] = CustomWebhookResponse
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
