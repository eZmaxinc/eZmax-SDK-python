"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.14
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.field_pki_secretquestion_id import FieldPkiSecretquestionID
from eZmaxApi.model.field_pki_taxassignment_id import FieldPkiTaxassignmentID
from eZmaxApi.model.field_pki_userlogintype_id import FieldPkiUserlogintypeID
globals()['FieldPkiSecretquestionID'] = FieldPkiSecretquestionID
globals()['FieldPkiTaxassignmentID'] = FieldPkiTaxassignmentID
globals()['FieldPkiUserlogintypeID'] = FieldPkiUserlogintypeID
from eZmaxApi.model.ezsignsigner_request import EzsignsignerRequest


class TestEzsignsignerRequest(unittest.TestCase):
    """EzsignsignerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsignsignerRequest(self):
        """Test EzsignsignerRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsignsignerRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
