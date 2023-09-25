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

from eZmaxApi.models.ezsignformfieldgroup_response_compound import EzsignformfieldgroupResponseCompound  # noqa: E501

class TestEzsignformfieldgroupResponseCompound(unittest.TestCase):
    """EzsignformfieldgroupResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignformfieldgroupResponseCompound:
        """Test EzsignformfieldgroupResponseCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignformfieldgroupResponseCompound`
        """
        model = EzsignformfieldgroupResponseCompound()  # noqa: E501
        if include_optional:
            return EzsignformfieldgroupResponseCompound(
                pki_ezsignformfieldgroup_id = 26,
                fki_ezsigndocument_id = 97,
                e_ezsignformfieldgroup_type = 'Text',
                e_ezsignformfieldgroup_signerrequirement = 'One',
                s_ezsignformfieldgroup_label = 'Allergies',
                i_ezsignformfieldgroup_step = 1,
                s_ezsignformfieldgroup_defaultvalue = 'Foo',
                i_ezsignformfieldgroup_filledmin = 1,
                i_ezsignformfieldgroup_filledmax = 2,
                b_ezsignformfieldgroup_readonly = True,
                i_ezsignformfieldgroup_maxlength = 75,
                b_ezsignformfieldgroup_encrypted = True,
                e_ezsignformfieldgroup_textvalidation = 'None',
                s_ezsignformfieldgroup_regexp = '/[-0-9a-zA-Z.+_]+@[-0-9a-zA-Z.+_]+.[a-zA-Z]{2,4}/',
                t_ezsignformfieldgroup_tooltip = 'Please enter a valid email address',
                e_ezsignformfieldgroup_tooltipposition = 'TopLeft',
                a_obj_ezsignformfield = [
                    eZmaxApi.models.ezsignformfield_response_compound.ezsignformfield-ResponseCompound()
                    ],
                a_obj_dropdown_element = [
                    eZmaxApi.models.custom_dropdown_element_response_compound.Custom-DropdownElement-ResponseCompound()
                    ],
                a_obj_ezsignformfieldgroupsigner = [
                    eZmaxApi.models.ezsignformfieldgroupsigner_response_compound.ezsignformfieldgroupsigner-ResponseCompound()
                    ]
            )
        else:
            return EzsignformfieldgroupResponseCompound(
                pki_ezsignformfieldgroup_id = 26,
                fki_ezsigndocument_id = 97,
                e_ezsignformfieldgroup_type = 'Text',
                e_ezsignformfieldgroup_signerrequirement = 'One',
                s_ezsignformfieldgroup_label = 'Allergies',
                i_ezsignformfieldgroup_step = 1,
                i_ezsignformfieldgroup_filledmin = 1,
                i_ezsignformfieldgroup_filledmax = 2,
                b_ezsignformfieldgroup_readonly = True,
                a_obj_ezsignformfield = [
                    eZmaxApi.models.ezsignformfield_response_compound.ezsignformfield-ResponseCompound()
                    ],
                a_obj_ezsignformfieldgroupsigner = [
                    eZmaxApi.models.ezsignformfieldgroupsigner_response_compound.ezsignformfieldgroupsigner-ResponseCompound()
                    ],
        )
        """

    def testEzsignformfieldgroupResponseCompound(self):
        """Test EzsignformfieldgroupResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
