"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.14
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.field_pki_ezsignfoldertype_id import FieldPkiEzsignfoldertypeID
from eZmaxApi.model.field_pki_ezsigntemplate_id import FieldPkiEzsigntemplateID
from eZmaxApi.model.field_pki_language_id import FieldPkiLanguageID
globals()['FieldPkiEzsignfoldertypeID'] = FieldPkiEzsignfoldertypeID
globals()['FieldPkiEzsigntemplateID'] = FieldPkiEzsigntemplateID
globals()['FieldPkiLanguageID'] = FieldPkiLanguageID
from eZmaxApi.model.ezsigntemplate_request import EzsigntemplateRequest


class TestEzsigntemplateRequest(unittest.TestCase):
    """EzsigntemplateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsigntemplateRequest(self):
        """Test EzsigntemplateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsigntemplateRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
