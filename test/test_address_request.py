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
from eZmaxApi.model.field_pki_addresstype_id import FieldPkiAddresstypeID
from eZmaxApi.model.field_pki_country_id import FieldPkiCountryID
from eZmaxApi.model.field_pki_province_id import FieldPkiProvinceID
globals()['FieldPkiAddresstypeID'] = FieldPkiAddresstypeID
globals()['FieldPkiCountryID'] = FieldPkiCountryID
globals()['FieldPkiProvinceID'] = FieldPkiProvinceID
from eZmaxApi.model.address_request import AddressRequest


class TestAddressRequest(unittest.TestCase):
    """AddressRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAddressRequest(self):
        """Test AddressRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AddressRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
