"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.12
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
from eZmaxApi.model.ezsignbulksend_reorder_v1_response import EzsignbulksendReorderV1Response


class TestEzsignbulksendReorderV1Response(unittest.TestCase):
    """EzsignbulksendReorderV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsignbulksendReorderV1Response(self):
        """Test EzsignbulksendReorderV1Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsignbulksendReorderV1Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
