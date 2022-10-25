"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.11
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.common_audit import CommonAudit
from eZmaxApi.model.field_e_user_type import FieldEUserType
from eZmaxApi.model.field_pki_language_id import FieldPkiLanguageID
from eZmaxApi.model.field_pki_user_id import FieldPkiUserID
globals()['CommonAudit'] = CommonAudit
globals()['FieldEUserType'] = FieldEUserType
globals()['FieldPkiLanguageID'] = FieldPkiLanguageID
globals()['FieldPkiUserID'] = FieldPkiUserID
from eZmaxApi.model.user_response import UserResponse


class TestUserResponse(unittest.TestCase):
    """UserResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserResponse(self):
        """Test UserResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
