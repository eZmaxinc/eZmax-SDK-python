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
from eZmaxApi.model.field_pki_contact_id import FieldPkiContactID
from eZmaxApi.model.field_pki_language_id import FieldPkiLanguageID
from eZmaxApi.model.field_s_phone_e164 import FieldSPhoneE164
globals()['FieldPkiContactID'] = FieldPkiContactID
globals()['FieldPkiLanguageID'] = FieldPkiLanguageID
globals()['FieldSPhoneE164'] = FieldSPhoneE164
from eZmaxApi.model.ezsignsigner_response_compound_contact import EzsignsignerResponseCompoundContact


class TestEzsignsignerResponseCompoundContact(unittest.TestCase):
    """EzsignsignerResponseCompoundContact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsignsignerResponseCompoundContact(self):
        """Test EzsignsignerResponseCompoundContact"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsignsignerResponseCompoundContact()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
