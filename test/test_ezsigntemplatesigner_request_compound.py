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
from eZmaxApi.model.ezsigntemplatesigner_request import EzsigntemplatesignerRequest
from eZmaxApi.model.field_pki_ezsigntemplate_id import FieldPkiEzsigntemplateID
from eZmaxApi.model.field_pki_ezsigntemplatesigner_id import FieldPkiEzsigntemplatesignerID
globals()['EzsigntemplatesignerRequest'] = EzsigntemplatesignerRequest
globals()['FieldPkiEzsigntemplateID'] = FieldPkiEzsigntemplateID
globals()['FieldPkiEzsigntemplatesignerID'] = FieldPkiEzsigntemplatesignerID
from eZmaxApi.model.ezsigntemplatesigner_request_compound import EzsigntemplatesignerRequestCompound


class TestEzsigntemplatesignerRequestCompound(unittest.TestCase):
    """EzsigntemplatesignerRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsigntemplatesignerRequestCompound(self):
        """Test EzsigntemplatesignerRequestCompound"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsigntemplatesignerRequestCompound()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
