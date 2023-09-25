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

from eZmaxApi.models.ezsignformfield_request_compound import EzsignformfieldRequestCompound  # noqa: E501

class TestEzsignformfieldRequestCompound(unittest.TestCase):
    """EzsignformfieldRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignformfieldRequestCompound:
        """Test EzsignformfieldRequestCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignformfieldRequestCompound`
        """
        model = EzsignformfieldRequestCompound()  # noqa: E501
        if include_optional:
            return EzsignformfieldRequestCompound(
                pki_ezsignformfield_id = 32,
                i_ezsignpage_pagenumber = 1,
                s_ezsignformfield_label = 'Peanuts',
                s_ezsignformfield_value = 'Yes',
                i_ezsignformfield_x = 200,
                i_ezsignformfield_y = 300,
                i_ezsignformfield_width = 102,
                i_ezsignformfield_height = 22,
                b_ezsignformfield_selected = True,
                s_ezsignformfield_enteredvalue = 'Montreal'
            )
        else:
            return EzsignformfieldRequestCompound(
                i_ezsignpage_pagenumber = 1,
                s_ezsignformfield_label = 'Peanuts',
                i_ezsignformfield_x = 200,
                i_ezsignformfield_y = 300,
                i_ezsignformfield_width = 102,
                i_ezsignformfield_height = 22,
        )
        """

    def testEzsignformfieldRequestCompound(self):
        """Test EzsignformfieldRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
