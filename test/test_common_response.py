"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.common_response_obj_debug import CommonResponseObjDebug
from eZmaxApi.model.common_response_obj_debug_payload import CommonResponseObjDebugPayload
globals()['CommonResponseObjDebug'] = CommonResponseObjDebug
globals()['CommonResponseObjDebugPayload'] = CommonResponseObjDebugPayload
from eZmaxApi.model.common_response import CommonResponse


class TestCommonResponse(unittest.TestCase):
    """CommonResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCommonResponse(self):
        """Test CommonResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CommonResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
