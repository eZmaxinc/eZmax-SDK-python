# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.1
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from eZmaxApi.models.ezsigntemplateformfieldgroup_response import EzsigntemplateformfieldgroupResponse

class TestEzsigntemplateformfieldgroupResponse(unittest.TestCase):
    """EzsigntemplateformfieldgroupResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplateformfieldgroupResponse:
        """Test EzsigntemplateformfieldgroupResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplateformfieldgroupResponse`
        """
        model = EzsigntemplateformfieldgroupResponse()
        if include_optional:
            return EzsigntemplateformfieldgroupResponse(
                pki_ezsigntemplateformfieldgroup_id = 64,
                fki_ezsigntemplatedocument_id = 133,
                e_ezsigntemplateformfieldgroup_type = 'Text',
                e_ezsigntemplateformfieldgroup_signerrequirement = 'One',
                s_ezsigntemplateformfieldgroup_label = 'Allergies',
                i_ezsigntemplateformfieldgroup_step = 1,
                s_ezsigntemplateformfieldgroup_defaultvalue = 'Foo',
                i_ezsigntemplateformfieldgroup_filledmin = 1,
                i_ezsigntemplateformfieldgroup_filledmax = 2,
                b_ezsigntemplateformfieldgroup_readonly = True,
                i_ezsigntemplateformfieldgroup_maxlength = 75,
                b_ezsigntemplateformfieldgroup_encrypted = True,
                s_ezsigntemplateformfieldgroup_regexp = '^.{0,30}$',
                s_ezsigntemplateformfieldgroup_textvalidationcustommessage = 'Phone number',
                e_ezsigntemplateformfieldgroup_textvalidation = 'None',
                t_ezsigntemplateformfieldgroup_tooltip = 'Please enter a valid email address',
                e_ezsigntemplateformfieldgroup_tooltipposition = 'TopLeft'
            )
        else:
            return EzsigntemplateformfieldgroupResponse(
                pki_ezsigntemplateformfieldgroup_id = 64,
                fki_ezsigntemplatedocument_id = 133,
                e_ezsigntemplateformfieldgroup_type = 'Text',
                s_ezsigntemplateformfieldgroup_label = 'Allergies',
                i_ezsigntemplateformfieldgroup_step = 1,
                i_ezsigntemplateformfieldgroup_filledmin = 1,
                i_ezsigntemplateformfieldgroup_filledmax = 2,
                b_ezsigntemplateformfieldgroup_readonly = True,
        )
        """

    def testEzsigntemplateformfieldgroupResponse(self):
        """Test EzsigntemplateformfieldgroupResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
