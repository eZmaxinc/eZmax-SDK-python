"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.10
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.common_audit import CommonAudit
from eZmaxApi.model.field_pki_ezsignbulksend_id import FieldPkiEzsignbulksendID
from eZmaxApi.model.field_pki_ezsignfoldertype_id import FieldPkiEzsignfoldertypeID
from eZmaxApi.model.field_pki_language_id import FieldPkiLanguageID
globals()['CommonAudit'] = CommonAudit
globals()['FieldPkiEzsignbulksendID'] = FieldPkiEzsignbulksendID
globals()['FieldPkiEzsignfoldertypeID'] = FieldPkiEzsignfoldertypeID
globals()['FieldPkiLanguageID'] = FieldPkiLanguageID
from eZmaxApi.model.ezsignbulksend_response import EzsignbulksendResponse


class TestEzsignbulksendResponse(unittest.TestCase):
    """EzsignbulksendResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsignbulksendResponse(self):
        """Test EzsignbulksendResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsignbulksendResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
