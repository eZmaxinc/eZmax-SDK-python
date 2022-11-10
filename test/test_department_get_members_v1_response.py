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
from eZmaxApi.model.department_get_members_v1_response_all_of import DepartmentGetMembersV1ResponseAllOf
from eZmaxApi.model.department_get_members_v1_response_m_payload import DepartmentGetMembersV1ResponseMPayload
globals()['CommonResponse'] = CommonResponse
globals()['CommonResponseObjDebug'] = CommonResponseObjDebug
globals()['CommonResponseObjDebugPayload'] = CommonResponseObjDebugPayload
globals()['DepartmentGetMembersV1ResponseAllOf'] = DepartmentGetMembersV1ResponseAllOf
globals()['DepartmentGetMembersV1ResponseMPayload'] = DepartmentGetMembersV1ResponseMPayload
from eZmaxApi.model.department_get_members_v1_response import DepartmentGetMembersV1Response


class TestDepartmentGetMembersV1Response(unittest.TestCase):
    """DepartmentGetMembersV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDepartmentGetMembersV1Response(self):
        """Test DepartmentGetMembersV1Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DepartmentGetMembersV1Response()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
