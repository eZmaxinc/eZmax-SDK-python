"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.7
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.common_audit import CommonAudit
from eZmaxApi.model.field_e_ezsigndocument_step import FieldEEzsigndocumentStep
from eZmaxApi.model.field_pki_language_id import FieldPkiLanguageID
globals()['CommonAudit'] = CommonAudit
globals()['FieldEEzsigndocumentStep'] = FieldEEzsigndocumentStep
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
