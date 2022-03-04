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
from eZmaxApi.model.ezsignsigner_request import EzsignsignerRequest
from eZmaxApi.model.ezsignsigner_request_compound_all_of import EzsignsignerRequestCompoundAllOf
from eZmaxApi.model.ezsignsigner_request_compound_contact import EzsignsignerRequestCompoundContact
from eZmaxApi.model.field_pki_taxassignment_id import FieldPkiTaxassignmentID
globals()['EzsignsignerRequest'] = EzsignsignerRequest
globals()['EzsignsignerRequestCompoundAllOf'] = EzsignsignerRequestCompoundAllOf
globals()['EzsignsignerRequestCompoundContact'] = EzsignsignerRequestCompoundContact
globals()['FieldPkiTaxassignmentID'] = FieldPkiTaxassignmentID
from eZmaxApi.model.ezsignsigner_request_compound import EzsignsignerRequestCompound


class TestEzsignsignerRequestCompound(unittest.TestCase):
    """EzsignsignerRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsignsignerRequestCompound(self):
        """Test EzsignsignerRequestCompound"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsignsignerRequestCompound()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
