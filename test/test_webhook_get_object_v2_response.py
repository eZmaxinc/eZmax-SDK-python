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
from eZmaxApi.model.webhook_get_object_v2_response_all_of import WebhookGetObjectV2ResponseAllOf
from eZmaxApi.model.webhook_get_object_v2_response_m_payload import WebhookGetObjectV2ResponseMPayload
globals()['CommonResponse'] = CommonResponse
globals()['CommonResponseObjDebug'] = CommonResponseObjDebug
globals()['CommonResponseObjDebugPayload'] = CommonResponseObjDebugPayload
globals()['WebhookGetObjectV2ResponseAllOf'] = WebhookGetObjectV2ResponseAllOf
globals()['WebhookGetObjectV2ResponseMPayload'] = WebhookGetObjectV2ResponseMPayload
from eZmaxApi.model.webhook_get_object_v2_response import WebhookGetObjectV2Response


class TestWebhookGetObjectV2Response(unittest.TestCase):
    """WebhookGetObjectV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWebhookGetObjectV2Response(self):
        """Test WebhookGetObjectV2Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WebhookGetObjectV2Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
