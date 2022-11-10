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
from eZmaxApi.model.common_response import CommonResponse
from eZmaxApi.model.common_response_obj_debug import CommonResponseObjDebug
from eZmaxApi.model.common_response_obj_debug_payload import CommonResponseObjDebugPayload
globals()['CommonResponse'] = CommonResponse
globals()['CommonResponseObjDebug'] = CommonResponseObjDebug
globals()['CommonResponseObjDebugPayload'] = CommonResponseObjDebugPayload
from eZmaxApi.model.webhook_delete_object_v1_response import WebhookDeleteObjectV1Response


class TestWebhookDeleteObjectV1Response(unittest.TestCase):
    """WebhookDeleteObjectV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWebhookDeleteObjectV1Response(self):
        """Test WebhookDeleteObjectV1Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WebhookDeleteObjectV1Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
