"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.31
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.model.contact_request import ContactRequest
from eZmaxinc/eZmax-SDK-python.model.contact_request_compound_all_of import ContactRequestCompoundAllOf
from eZmaxinc/eZmax-SDK-python.model.contactinformations_request_compound import ContactinformationsRequestCompound
from eZmaxinc/eZmax-SDK-python.model.field_pki_language_id import FieldPkiLanguageID
globals()['ContactRequest'] = ContactRequest
globals()['ContactRequestCompoundAllOf'] = ContactRequestCompoundAllOf
globals()['ContactinformationsRequestCompound'] = ContactinformationsRequestCompound
globals()['FieldPkiLanguageID'] = FieldPkiLanguageID
from eZmaxinc/eZmax-SDK-python.model.contact_request_compound import ContactRequestCompound


class TestContactRequestCompound(unittest.TestCase):
    """ContactRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testContactRequestCompound(self):
        """Test ContactRequestCompound"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ContactRequestCompound()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
