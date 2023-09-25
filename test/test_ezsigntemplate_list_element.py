# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.0
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from eZmaxApi.models.ezsigntemplate_list_element import EzsigntemplateListElement  # noqa: E501

class TestEzsigntemplateListElement(unittest.TestCase):
    """EzsigntemplateListElement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplateListElement:
        """Test EzsigntemplateListElement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplateListElement`
        """
        model = EzsigntemplateListElement()  # noqa: E501
        if include_optional:
            return EzsigntemplateListElement(
                pki_ezsigntemplate_id = 36,
                fki_ezsignfoldertype_id = 5,
                fki_language_id = 2,
                s_ezsigntemplate_description = 'Standard Contract',
                i_ezsigntemplatedocument_pagetotal = 5,
                i_ezsigntemplate_signaturetotal = 8,
                i_ezsigntemplate_formfieldtotal = 8,
                b_ezsigntemplate_incomplete = False,
                s_ezsignfoldertype_name_x = 'Default'
            )
        else:
            return EzsigntemplateListElement(
                pki_ezsigntemplate_id = 36,
                fki_ezsignfoldertype_id = 5,
                fki_language_id = 2,
                s_ezsigntemplate_description = 'Standard Contract',
                b_ezsigntemplate_incomplete = False,
                s_ezsignfoldertype_name_x = 'Default',
        )
        """

    def testEzsigntemplateListElement(self):
        """Test EzsigntemplateListElement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
