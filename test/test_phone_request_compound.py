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
from eZmaxApi.model.field_e_phone_type import FieldEPhoneType
from eZmaxApi.model.field_pki_phonetype_id import FieldPkiPhonetypeID
from eZmaxApi.model.field_s_phone_e164 import FieldSPhoneE164
from eZmaxApi.model.phone_request import PhoneRequest
globals()['FieldEPhoneType'] = FieldEPhoneType
globals()['FieldPkiPhonetypeID'] = FieldPkiPhonetypeID
globals()['FieldSPhoneE164'] = FieldSPhoneE164
globals()['PhoneRequest'] = PhoneRequest
from eZmaxApi.model.phone_request_compound import PhoneRequestCompound


class TestPhoneRequestCompound(unittest.TestCase):
    """PhoneRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPhoneRequestCompound(self):
        """Test PhoneRequestCompound"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PhoneRequestCompound()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
