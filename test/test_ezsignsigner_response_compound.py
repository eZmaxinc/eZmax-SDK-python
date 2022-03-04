"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.6
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.ezsignsigner_response import EzsignsignerResponse
from eZmaxApi.model.ezsignsigner_response_compound_all_of import EzsignsignerResponseCompoundAllOf
from eZmaxApi.model.ezsignsigner_response_compound_contact import EzsignsignerResponseCompoundContact
from eZmaxApi.model.field_pki_taxassignment_id import FieldPkiTaxassignmentID
globals()['EzsignsignerResponse'] = EzsignsignerResponse
globals()['EzsignsignerResponseCompoundAllOf'] = EzsignsignerResponseCompoundAllOf
globals()['EzsignsignerResponseCompoundContact'] = EzsignsignerResponseCompoundContact
globals()['FieldPkiTaxassignmentID'] = FieldPkiTaxassignmentID
from eZmaxApi.model.ezsignsigner_response_compound import EzsignsignerResponseCompound


class TestEzsignsignerResponseCompound(unittest.TestCase):
    """EzsignsignerResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsignsignerResponseCompound(self):
        """Test EzsignsignerResponseCompound"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsignsignerResponseCompound()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
