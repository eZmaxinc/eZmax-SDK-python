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
from eZmaxApi.model.field_pki_ezsigntemplatepackage_id import FieldPkiEzsigntemplatepackageID
from eZmaxApi.model.field_pki_ezsigntemplatepackagesigner_id import FieldPkiEzsigntemplatepackagesignerID
globals()['FieldPkiEzsigntemplatepackageID'] = FieldPkiEzsigntemplatepackageID
globals()['FieldPkiEzsigntemplatepackagesignerID'] = FieldPkiEzsigntemplatepackagesignerID
from eZmaxApi.model.ezsigntemplatepackagesigner_request import EzsigntemplatepackagesignerRequest


class TestEzsigntemplatepackagesignerRequest(unittest.TestCase):
    """EzsigntemplatepackagesignerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsigntemplatepackagesignerRequest(self):
        """Test EzsigntemplatepackagesignerRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsigntemplatepackagesignerRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
