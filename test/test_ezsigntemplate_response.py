"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.12
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.field_pki_ezsignfoldertype_id import FieldPkiEzsignfoldertypeID
from eZmaxApi.model.field_pki_ezsigntemplate_id import FieldPkiEzsigntemplateID
from eZmaxApi.model.field_pki_ezsigntemplatedocument_id import FieldPkiEzsigntemplatedocumentID
from eZmaxApi.model.field_pki_language_id import FieldPkiLanguageID
globals()['FieldPkiEzsignfoldertypeID'] = FieldPkiEzsignfoldertypeID
globals()['FieldPkiEzsigntemplateID'] = FieldPkiEzsigntemplateID
globals()['FieldPkiEzsigntemplatedocumentID'] = FieldPkiEzsigntemplatedocumentID
globals()['FieldPkiLanguageID'] = FieldPkiLanguageID
from eZmaxApi.model.ezsigntemplate_response import EzsigntemplateResponse


class TestEzsigntemplateResponse(unittest.TestCase):
    """EzsigntemplateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsigntemplateResponse(self):
        """Test EzsigntemplateResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsigntemplateResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
