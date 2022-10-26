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
from eZmaxApi.model.common_audit import CommonAudit
from eZmaxApi.model.field_e_ezsigndocument_step import FieldEEzsigndocumentStep
from eZmaxApi.model.field_i_ezsigndocument_order import FieldIEzsigndocumentOrder
from eZmaxApi.model.field_i_ezsigndocument_pagetotal import FieldIEzsigndocumentPagetotal
from eZmaxApi.model.field_i_ezsigndocument_signaturesigned import FieldIEzsigndocumentSignaturesigned
from eZmaxApi.model.field_i_ezsigndocument_signaturetotal import FieldIEzsigndocumentSignaturetotal
from eZmaxApi.model.field_pki_ezsigndocument_id import FieldPkiEzsigndocumentID
from eZmaxApi.model.field_pki_ezsignfolder_id import FieldPkiEzsignfolderID
from eZmaxApi.model.field_pki_language_id import FieldPkiLanguageID
globals()['CommonAudit'] = CommonAudit
globals()['FieldEEzsigndocumentStep'] = FieldEEzsigndocumentStep
globals()['FieldIEzsigndocumentOrder'] = FieldIEzsigndocumentOrder
globals()['FieldIEzsigndocumentPagetotal'] = FieldIEzsigndocumentPagetotal
globals()['FieldIEzsigndocumentSignaturesigned'] = FieldIEzsigndocumentSignaturesigned
globals()['FieldIEzsigndocumentSignaturetotal'] = FieldIEzsigndocumentSignaturetotal
globals()['FieldPkiEzsigndocumentID'] = FieldPkiEzsigndocumentID
globals()['FieldPkiEzsignfolderID'] = FieldPkiEzsignfolderID
globals()['FieldPkiLanguageID'] = FieldPkiLanguageID
from eZmaxApi.model.ezsigndocument_response import EzsigndocumentResponse


class TestEzsigndocumentResponse(unittest.TestCase):
    """EzsigndocumentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsigndocumentResponse(self):
        """Test EzsigndocumentResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsigndocumentResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
