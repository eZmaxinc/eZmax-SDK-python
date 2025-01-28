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

from eZmaxApi.models.ezsigntemplatesignature_request_compound_v2 import EzsigntemplatesignatureRequestCompoundV2

class TestEzsigntemplatesignatureRequestCompoundV2(unittest.TestCase):
    """EzsigntemplatesignatureRequestCompoundV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatesignatureRequestCompoundV2:
        """Test EzsigntemplatesignatureRequestCompoundV2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatesignatureRequestCompoundV2`
        """
        model = EzsigntemplatesignatureRequestCompoundV2()
        if include_optional:
            return EzsigntemplatesignatureRequestCompoundV2(
                pki_ezsigntemplatesignature_id = 99,
                fki_ezsigntemplatedocument_id = 133,
                fki_ezsigntemplatesigner_id = 9,
                fki_ezsigntemplatesigner_id_validation = 9,
                b_ezsigntemplatesignature_handwritten = True,
                b_ezsigntemplatesignature_reason = True,
                e_ezsigntemplatesignature_positioning = 'PerCoordinates',
                i_ezsigntemplatedocumentpage_pagenumber = 1,
                i_ezsigntemplatesignature_x = 200,
                i_ezsigntemplatesignature_y = 300,
                i_ezsigntemplatesignature_width = 200,
                i_ezsigntemplatesignature_height = 200,
                i_ezsigntemplatesignature_step = 1,
                e_ezsigntemplatesignature_type = 'Signature',
                e_ezsigntemplatesignature_consultationtrigger = 'Manual',
                t_ezsigntemplatesignature_tooltip = 'Please sign here if you agree to the terms',
                e_ezsigntemplatesignature_tooltipposition = 'TopLeft',
                e_ezsigntemplatesignature_font = 'Normal',
                b_ezsigntemplatesignature_required = True,
                e_ezsigntemplatesignature_attachmentnamesource = 'Description',
                s_ezsigntemplatesignature_attachmentdescription = 'Attachment',
                i_ezsigntemplatesignature_validationstep = 1,
                i_ezsigntemplatesignature_maxlength = 75,
                s_ezsigntemplatesignature_defaultvalue = 'Foo',
                s_ezsigntemplatesignature_regexp = '^.{0,30}$',
                e_ezsigntemplatesignature_textvalidation = 'None',
                s_ezsigntemplatesignature_textvalidationcustommessage = 'Phone number',
                e_ezsigntemplatesignature_dependencyrequirement = 'AllOf',
                s_ezsigntemplatesignature_positioningpattern = 'Signature',
                i_ezsigntemplatesignature_positioningoffsetx = 200,
                i_ezsigntemplatesignature_positioningoffsety = 200,
                e_ezsigntemplatesignature_positioningoccurence = 'All',
                b_ezsigntemplatesignature_customdate = True,
                a_obj_ezsigntemplatesignaturecustomdate = [
                    eZmaxApi.models.ezsigntemplatesignaturecustomdate_request_compound_v2.ezsigntemplatesignaturecustomdate-RequestCompoundV2()
                    ],
                a_obj_ezsigntemplateelementdependency = [
                    eZmaxApi.models.ezsigntemplateelementdependency_request_compound.ezsigntemplateelementdependency-RequestCompound()
                    ]
            )
        else:
            return EzsigntemplatesignatureRequestCompoundV2(
                fki_ezsigntemplatedocument_id = 133,
                fki_ezsigntemplatesigner_id = 9,
                i_ezsigntemplatedocumentpage_pagenumber = 1,
                i_ezsigntemplatesignature_step = 1,
                e_ezsigntemplatesignature_type = 'Signature',
        )
        """

    def testEzsigntemplatesignatureRequestCompoundV2(self):
        """Test EzsigntemplatesignatureRequestCompoundV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
