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
from eZmaxApi.model.field_e_phone_type import FieldEPhoneType
from eZmaxApi.model.field_pki_phonetype_id import FieldPkiPhonetypeID
from eZmaxApi.model.field_s_phone_e164 import FieldSPhoneE164
globals()['FieldEPhoneType'] = FieldEPhoneType
globals()['FieldPkiPhonetypeID'] = FieldPkiPhonetypeID
globals()['FieldSPhoneE164'] = FieldSPhoneE164
from eZmaxApi.model.phone_request import PhoneRequest


class TestPhoneRequest(unittest.TestCase):
    """PhoneRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPhoneRequest(self):
        """Test PhoneRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PhoneRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
