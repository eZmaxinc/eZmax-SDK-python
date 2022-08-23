"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.10
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.common_response import CommonResponse
from eZmaxApi.model.common_response_obj_debug import CommonResponseObjDebug
from eZmaxApi.model.common_response_obj_debug_payload import CommonResponseObjDebugPayload
from eZmaxApi.model.webhook_get_object_v1_response_all_of import WebhookGetObjectV1ResponseAllOf
from eZmaxApi.model.webhook_get_object_v1_response_m_payload import WebhookGetObjectV1ResponseMPayload
globals()['CommonResponse'] = CommonResponse
globals()['CommonResponseObjDebug'] = CommonResponseObjDebug
globals()['CommonResponseObjDebugPayload'] = CommonResponseObjDebugPayload
globals()['WebhookGetObjectV1ResponseAllOf'] = WebhookGetObjectV1ResponseAllOf
globals()['WebhookGetObjectV1ResponseMPayload'] = WebhookGetObjectV1ResponseMPayload
from eZmaxApi.model.webhook_get_object_v1_response import WebhookGetObjectV1Response


class TestWebhookGetObjectV1Response(unittest.TestCase):
    """WebhookGetObjectV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWebhookGetObjectV1Response(self):
        """Test WebhookGetObjectV1Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WebhookGetObjectV1Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
