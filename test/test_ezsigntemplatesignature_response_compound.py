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

from eZmaxApi.models.ezsigntemplatesignature_response_compound import EzsigntemplatesignatureResponseCompound  # noqa: E501

class TestEzsigntemplatesignatureResponseCompound(unittest.TestCase):
    """EzsigntemplatesignatureResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatesignatureResponseCompound:
        """Test EzsigntemplatesignatureResponseCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatesignatureResponseCompound`
        """
        model = EzsigntemplatesignatureResponseCompound()  # noqa: E501
        if include_optional:
            return EzsigntemplatesignatureResponseCompound(
                pki_ezsigntemplatesignature_id = 99,
                fki_ezsigntemplatedocument_id = 133,
                fki_ezsigntemplatesigner_id = 9,
                fki_ezsigntemplatesigner_id_validation = 9,
                i_ezsigntemplatedocumentpage_pagenumber = 1,
                i_ezsigntemplatesignature_x = 200,
                i_ezsigntemplatesignature_y = 300,
                i_ezsigntemplatesignature_width = 200,
                i_ezsigntemplatesignature_height = 200,
                i_ezsigntemplatesignature_step = 1,
                e_ezsigntemplatesignature_type = 'Name',
                t_ezsigntemplatesignature_tooltip = 'Please sign here if you agree to the terms',
                e_ezsigntemplatesignature_tooltipposition = 'TopLeft',
                e_ezsigntemplatesignature_font = 'Normal',
                i_ezsigntemplatesignature_validationstep = 1,
                s_ezsigntemplatesignature_attachmentdescription = 'Attachment',
                e_ezsigntemplatesignature_attachmentnamesource = 'Description',
                b_ezsigntemplatesignature_required = True,
                i_ezsigntemplatesignature_maxlength = 75,
                s_ezsigntemplatesignature_regexp = '/[-0-9a-zA-Z.+_]+@[-0-9a-zA-Z.+_]+.[a-zA-Z]{2,4}/',
                e_ezsigntemplatesignature_textvalidation = 'None',
                e_ezsigntemplatesignature_dependencyrequirement = 'AllOf',
                b_ezsigntemplatesignature_customdate = True,
                a_obj_ezsigntemplatesignaturecustomdate = [
                    eZmaxApi.models.ezsigntemplatesignaturecustomdate_response_compound.ezsigntemplatesignaturecustomdate-ResponseCompound()
                    ],
                a_obj_ezsigntemplateelementdependency = [
                    eZmaxApi.models.ezsigntemplateelementdependency_response_compound.ezsigntemplateelementdependency-ResponseCompound()
                    ]
            )
        else:
            return EzsigntemplatesignatureResponseCompound(
                pki_ezsigntemplatesignature_id = 99,
                fki_ezsigntemplatedocument_id = 133,
                fki_ezsigntemplatesigner_id = 9,
                i_ezsigntemplatedocumentpage_pagenumber = 1,
                i_ezsigntemplatesignature_x = 200,
                i_ezsigntemplatesignature_y = 300,
                i_ezsigntemplatesignature_step = 1,
                e_ezsigntemplatesignature_type = 'Name',
        )
        """

    def testEzsigntemplatesignatureResponseCompound(self):
        """Test EzsigntemplatesignatureResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
