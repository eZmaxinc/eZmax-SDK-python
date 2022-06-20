"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.8
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
from eZmaxApi.model.user_response import UserResponse
globals()['CommonAudit'] = CommonAudit
globals()['FieldEUserType'] = FieldEUserType
globals()['FieldPkiLanguageID'] = FieldPkiLanguageID
globals()['FieldPkiUserID'] = FieldPkiUserID
globals()['UserResponse'] = UserResponse
from eZmaxApi.model.user_response_compound import UserResponseCompound


class TestUserResponseCompound(unittest.TestCase):
    """UserResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserResponseCompound(self):
        """Test UserResponseCompound"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserResponseCompound()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
