"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.9
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
from eZmaxApi.model.ezsignfolder_unsend_v1_response import EzsignfolderUnsendV1Response


class TestEzsignfolderUnsendV1Response(unittest.TestCase):
    """EzsignfolderUnsendV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsignfolderUnsendV1Response(self):
        """Test EzsignfolderUnsendV1Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsignfolderUnsendV1Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
