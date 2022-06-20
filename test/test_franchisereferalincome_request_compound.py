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
from eZmaxApi.model.address_request import AddressRequest
from eZmaxApi.model.contact_request_compound import ContactRequestCompound
from eZmaxApi.model.field_pki_franchisebroker_id import FieldPkiFranchisebrokerID
from eZmaxApi.model.field_pki_franchiseoffice_id import FieldPkiFranchiseofficeID
from eZmaxApi.model.field_pki_franchisereferalincome_id import FieldPkiFranchisereferalincomeID
from eZmaxApi.model.field_pki_franchisereferalincomeprogram_id import FieldPkiFranchisereferalincomeprogramID
from eZmaxApi.model.field_pki_period_id import FieldPkiPeriodID
from eZmaxApi.model.franchisereferalincome_request import FranchisereferalincomeRequest
from eZmaxApi.model.franchisereferalincome_request_compound_all_of import FranchisereferalincomeRequestCompoundAllOf
globals()['AddressRequest'] = AddressRequest
globals()['ContactRequestCompound'] = ContactRequestCompound
globals()['FieldPkiFranchisebrokerID'] = FieldPkiFranchisebrokerID
globals()['FieldPkiFranchiseofficeID'] = FieldPkiFranchiseofficeID
globals()['FieldPkiFranchisereferalincomeID'] = FieldPkiFranchisereferalincomeID
globals()['FieldPkiFranchisereferalincomeprogramID'] = FieldPkiFranchisereferalincomeprogramID
globals()['FieldPkiPeriodID'] = FieldPkiPeriodID
globals()['FranchisereferalincomeRequest'] = FranchisereferalincomeRequest
globals()['FranchisereferalincomeRequestCompoundAllOf'] = FranchisereferalincomeRequestCompoundAllOf
from eZmaxApi.model.franchisereferalincome_request_compound import FranchisereferalincomeRequestCompound


class TestFranchisereferalincomeRequestCompound(unittest.TestCase):
    """FranchisereferalincomeRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFranchisereferalincomeRequestCompound(self):
        """Test FranchisereferalincomeRequestCompound"""
        # FIXME: construct object with mandatory attributes with example values
        # model = FranchisereferalincomeRequestCompound()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
