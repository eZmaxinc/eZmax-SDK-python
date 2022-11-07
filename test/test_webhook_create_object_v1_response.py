"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.15
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.common_response import CommonResponse
from eZmaxApi.model.common_response_obj_debug import CommonResponseObjDebug
from eZmaxApi.model.common_response_obj_debug_payload import CommonResponseObjDebugPayload
from eZmaxApi.model.webhook_create_object_v1_response_all_of import WebhookCreateObjectV1ResponseAllOf
from eZmaxApi.model.webhook_create_object_v1_response_m_payload import WebhookCreateObjectV1ResponseMPayload
globals()['CommonResponse'] = CommonResponse
globals()['CommonResponseObjDebug'] = CommonResponseObjDebug
globals()['CommonResponseObjDebugPayload'] = CommonResponseObjDebugPayload
globals()['WebhookCreateObjectV1ResponseAllOf'] = WebhookCreateObjectV1ResponseAllOf
globals()['WebhookCreateObjectV1ResponseMPayload'] = WebhookCreateObjectV1ResponseMPayload
from eZmaxApi.model.webhook_create_object_v1_response import WebhookCreateObjectV1Response


class TestWebhookCreateObjectV1Response(unittest.TestCase):
    """WebhookCreateObjectV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWebhookCreateObjectV1Response(self):
        """Test WebhookCreateObjectV1Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WebhookCreateObjectV1Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
