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
from eZmaxApi.model.field_pki_ezsignfoldertype_id import FieldPkiEzsignfoldertypeID
from eZmaxApi.model.field_pki_ezsigntemplatepackage_id import FieldPkiEzsigntemplatepackageID
from eZmaxApi.model.field_pki_language_id import FieldPkiLanguageID
globals()['FieldPkiEzsignfoldertypeID'] = FieldPkiEzsignfoldertypeID
globals()['FieldPkiEzsigntemplatepackageID'] = FieldPkiEzsigntemplatepackageID
globals()['FieldPkiLanguageID'] = FieldPkiLanguageID
from eZmaxApi.model.ezsigntemplatepackage_response import EzsigntemplatepackageResponse


class TestEzsigntemplatepackageResponse(unittest.TestCase):
    """EzsigntemplatepackageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsigntemplatepackageResponse(self):
        """Test EzsigntemplatepackageResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsigntemplatepackageResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
