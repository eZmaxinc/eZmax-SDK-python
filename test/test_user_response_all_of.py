"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.39
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.common_audit import CommonAudit
from eZmaxApi.model.field_e_user_type import FieldEUserType
from eZmaxApi.model.field_pki_language_id import FieldPkiLanguageID
globals()['CommonAudit'] = CommonAudit
globals()['FieldEUserType'] = FieldEUserType
globals()['FieldPkiLanguageID'] = FieldPkiLanguageID
from eZmaxApi.model.user_response_all_of import UserResponseAllOf


class TestUserResponseAllOf(unittest.TestCase):
    """UserResponseAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserResponseAllOf(self):
        """Test UserResponseAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserResponseAllOf()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
