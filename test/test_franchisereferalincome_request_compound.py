"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.45
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.address_request import AddressRequest
from eZmaxApi.model.contact_request_compound import ContactRequestCompound
from eZmaxApi.model.franchisereferalincome_request import FranchisereferalincomeRequest
globals()['AddressRequest'] = AddressRequest
globals()['ContactRequestCompound'] = ContactRequestCompound
globals()['FranchisereferalincomeRequest'] = FranchisereferalincomeRequest
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
