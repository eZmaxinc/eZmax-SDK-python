"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.48
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.field_e_user_type_sspr import FieldEUserTypeSSPR
from eZmaxApi.model.field_pki_language_id import FieldPkiLanguageID
from eZmaxApi.model.field_pks_customer_code import FieldPksCustomerCode
globals()['FieldEUserTypeSSPR'] = FieldEUserTypeSSPR
globals()['FieldPkiLanguageID'] = FieldPkiLanguageID
globals()['FieldPksCustomerCode'] = FieldPksCustomerCode
from eZmaxApi.model.sspr_send_usernames_v1_request import SsprSendUsernamesV1Request


class TestSsprSendUsernamesV1Request(unittest.TestCase):
    """SsprSendUsernamesV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSsprSendUsernamesV1Request(self):
        """Test SsprSendUsernamesV1Request"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SsprSendUsernamesV1Request()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
