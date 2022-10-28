"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.13
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.branding_get_object_v1_response_all_of import BrandingGetObjectV1ResponseAllOf
from eZmaxApi.model.branding_get_object_v1_response_m_payload import BrandingGetObjectV1ResponseMPayload
from eZmaxApi.model.common_response import CommonResponse
from eZmaxApi.model.common_response_obj_debug import CommonResponseObjDebug
from eZmaxApi.model.common_response_obj_debug_payload import CommonResponseObjDebugPayload
globals()['BrandingGetObjectV1ResponseAllOf'] = BrandingGetObjectV1ResponseAllOf
globals()['BrandingGetObjectV1ResponseMPayload'] = BrandingGetObjectV1ResponseMPayload
globals()['CommonResponse'] = CommonResponse
globals()['CommonResponseObjDebug'] = CommonResponseObjDebug
globals()['CommonResponseObjDebugPayload'] = CommonResponseObjDebugPayload
from eZmaxApi.model.branding_get_object_v1_response import BrandingGetObjectV1Response


class TestBrandingGetObjectV1Response(unittest.TestCase):
    """BrandingGetObjectV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBrandingGetObjectV1Response(self):
        """Test BrandingGetObjectV1Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BrandingGetObjectV1Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
