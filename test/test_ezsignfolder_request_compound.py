"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.15
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.ezsignfolder_request import EzsignfolderRequest
from eZmaxApi.model.field_e_ezsignfolder_sendreminderfrequency import FieldEEzsignfolderSendreminderfrequency
from eZmaxApi.model.field_pki_ezsignfolder_id import FieldPkiEzsignfolderID
from eZmaxApi.model.field_pki_ezsignfoldertype_id import FieldPkiEzsignfoldertypeID
from eZmaxApi.model.field_pki_ezsigntsarequirement_id import FieldPkiEzsigntsarequirementID
globals()['EzsignfolderRequest'] = EzsignfolderRequest
globals()['FieldEEzsignfolderSendreminderfrequency'] = FieldEEzsignfolderSendreminderfrequency
globals()['FieldPkiEzsignfolderID'] = FieldPkiEzsignfolderID
globals()['FieldPkiEzsignfoldertypeID'] = FieldPkiEzsignfoldertypeID
globals()['FieldPkiEzsigntsarequirementID'] = FieldPkiEzsigntsarequirementID
from eZmaxApi.model.ezsignfolder_request_compound import EzsignfolderRequestCompound


class TestEzsignfolderRequestCompound(unittest.TestCase):
    """EzsignfolderRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsignfolderRequestCompound(self):
        """Test EzsignfolderRequestCompound"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsignfolderRequestCompound()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
