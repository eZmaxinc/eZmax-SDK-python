"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.field_e_phone_type import FieldEPhoneType
globals()['FieldEPhoneType'] = FieldEPhoneType
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
