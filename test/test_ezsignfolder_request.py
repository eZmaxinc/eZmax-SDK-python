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
from eZmaxApi.model.field_e_ezsignfolder_sendreminderfrequency import FieldEEzsignfolderSendreminderfrequency
from eZmaxApi.model.field_pki_ezsigntsarequirement_id import FieldPkiEzsigntsarequirementID
globals()['FieldEEzsignfolderSendreminderfrequency'] = FieldEEzsignfolderSendreminderfrequency
globals()['FieldPkiEzsigntsarequirementID'] = FieldPkiEzsigntsarequirementID
from eZmaxApi.model.ezsignfolder_request import EzsignfolderRequest


class TestEzsignfolderRequest(unittest.TestCase):
    """EzsignfolderRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsignfolderRequest(self):
        """Test EzsignfolderRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsignfolderRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
