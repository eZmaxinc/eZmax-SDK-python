"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.9
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.field_e_activesession_usertype import FieldEActivesessionUsertype
from eZmaxApi.model.field_e_activesession_weekdaystart import FieldEActivesessionWeekdaystart
from eZmaxApi.model.field_pki_language_id import FieldPkiLanguageID
from eZmaxApi.model.field_pks_customer_code import FieldPksCustomerCode
globals()['FieldEActivesessionUsertype'] = FieldEActivesessionUsertype
globals()['FieldEActivesessionWeekdaystart'] = FieldEActivesessionWeekdaystart
globals()['FieldPkiLanguageID'] = FieldPkiLanguageID
globals()['FieldPksCustomerCode'] = FieldPksCustomerCode
from eZmaxApi.model.activesession_response import ActivesessionResponse


class TestActivesessionResponse(unittest.TestCase):
    """ActivesessionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testActivesessionResponse(self):
        """Test ActivesessionResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ActivesessionResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
