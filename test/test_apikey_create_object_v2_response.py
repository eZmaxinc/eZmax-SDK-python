"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.7
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.apikey_create_object_v2_response_all_of import ApikeyCreateObjectV2ResponseAllOf
from eZmaxApi.model.apikey_create_object_v2_response_m_payload import ApikeyCreateObjectV2ResponseMPayload
from eZmaxApi.model.common_response import CommonResponse
from eZmaxApi.model.common_response_obj_debug import CommonResponseObjDebug
from eZmaxApi.model.common_response_obj_debug_payload import CommonResponseObjDebugPayload
globals()['ApikeyCreateObjectV2ResponseAllOf'] = ApikeyCreateObjectV2ResponseAllOf
globals()['ApikeyCreateObjectV2ResponseMPayload'] = ApikeyCreateObjectV2ResponseMPayload
globals()['CommonResponse'] = CommonResponse
globals()['CommonResponseObjDebug'] = CommonResponseObjDebug
globals()['CommonResponseObjDebugPayload'] = CommonResponseObjDebugPayload
from eZmaxApi.model.apikey_create_object_v2_response import ApikeyCreateObjectV2Response


class TestApikeyCreateObjectV2Response(unittest.TestCase):
    """ApikeyCreateObjectV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApikeyCreateObjectV2Response(self):
        """Test ApikeyCreateObjectV2Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApikeyCreateObjectV2Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
