"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.8
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.field_pki_ezsigndocument_id import FieldPkiEzsigndocumentID
from eZmaxApi.model.field_pki_ezsignfolder_id import FieldPkiEzsignfolderID
from eZmaxApi.model.field_pki_ezsignfoldersignerassociation_id import FieldPkiEzsignfoldersignerassociationID
from eZmaxApi.model.field_pki_ezsigntemplate_id import FieldPkiEzsigntemplateID
from eZmaxApi.model.field_pki_language_id import FieldPkiLanguageID
globals()['FieldPkiEzsigndocumentID'] = FieldPkiEzsigndocumentID
globals()['FieldPkiEzsignfolderID'] = FieldPkiEzsignfolderID
globals()['FieldPkiEzsignfoldersignerassociationID'] = FieldPkiEzsignfoldersignerassociationID
globals()['FieldPkiEzsigntemplateID'] = FieldPkiEzsigntemplateID
globals()['FieldPkiLanguageID'] = FieldPkiLanguageID
from eZmaxApi.model.ezsigndocument_request import EzsigndocumentRequest


class TestEzsigndocumentRequest(unittest.TestCase):
    """EzsigndocumentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsigndocumentRequest(self):
        """Test EzsigndocumentRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsigndocumentRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
