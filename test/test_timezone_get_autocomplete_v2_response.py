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
from eZmaxApi.model.timezone_get_autocomplete_v2_response_all_of import TimezoneGetAutocompleteV2ResponseAllOf
from eZmaxApi.model.timezone_get_autocomplete_v2_response_m_payload import TimezoneGetAutocompleteV2ResponseMPayload
globals()['CommonResponse'] = CommonResponse
globals()['CommonResponseObjDebug'] = CommonResponseObjDebug
globals()['CommonResponseObjDebugPayload'] = CommonResponseObjDebugPayload
globals()['TimezoneGetAutocompleteV2ResponseAllOf'] = TimezoneGetAutocompleteV2ResponseAllOf
globals()['TimezoneGetAutocompleteV2ResponseMPayload'] = TimezoneGetAutocompleteV2ResponseMPayload
from eZmaxApi.model.timezone_get_autocomplete_v2_response import TimezoneGetAutocompleteV2Response


class TestTimezoneGetAutocompleteV2Response(unittest.TestCase):
    """TimezoneGetAutocompleteV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTimezoneGetAutocompleteV2Response(self):
        """Test TimezoneGetAutocompleteV2Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TimezoneGetAutocompleteV2Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
