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
from eZmaxApi.model.field_pki_contacttitle_id import FieldPkiContacttitleID
from eZmaxApi.model.field_pki_language_id import FieldPkiLanguageID
globals()['FieldPkiContacttitleID'] = FieldPkiContacttitleID
globals()['FieldPkiLanguageID'] = FieldPkiLanguageID
from eZmaxApi.model.contact_request import ContactRequest


class TestContactRequest(unittest.TestCase):
    """ContactRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testContactRequest(self):
        """Test ContactRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ContactRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
