"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.4
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.field_e_ezsignfolder_step import FieldEEzsignfolderStep
from eZmaxApi.model.field_e_ezsignfoldertype_privacylevel import FieldEEzsignfoldertypePrivacylevel
globals()['FieldEEzsignfolderStep'] = FieldEEzsignfolderStep
globals()['FieldEEzsignfoldertypePrivacylevel'] = FieldEEzsignfoldertypePrivacylevel
from eZmaxApi.model.ezsignfolder_list_element import EzsignfolderListElement


class TestEzsignfolderListElement(unittest.TestCase):
    """EzsignfolderListElement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsignfolderListElement(self):
        """Test EzsignfolderListElement"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsignfolderListElement()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
