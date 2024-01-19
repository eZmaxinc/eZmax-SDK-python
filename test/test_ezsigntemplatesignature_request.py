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

from eZmaxApi.models.ezsigntemplatesignature_request import EzsigntemplatesignatureRequest

class TestEzsigntemplatesignatureRequest(unittest.TestCase):
    """EzsigntemplatesignatureRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatesignatureRequest:
        """Test EzsigntemplatesignatureRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatesignatureRequest`
        """
        model = EzsigntemplatesignatureRequest()
        if include_optional:
            return EzsigntemplatesignatureRequest(
                pki_ezsigntemplatesignature_id = 99,
                fki_ezsigntemplatedocument_id = 133,
                fki_ezsigntemplatesigner_id = 9,
                fki_ezsigntemplatesigner_id_validation = 9,
                e_ezsigntemplatesignature_positioning = 'PerCoordinates',
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
                b_ezsigntemplatesignature_required = True,
                e_ezsigntemplatesignature_attachmentnamesource = 'Description',
                s_ezsigntemplatesignature_attachmentdescription = 'Attachment',
                i_ezsigntemplatesignature_validationstep = 1,
                i_ezsigntemplatesignature_maxlength = 75,
                s_ezsigntemplatesignature_regexp = '/[-0-9a-zA-Z.+_]+@[-0-9a-zA-Z.+_]+.[a-zA-Z]{2,4}/',
                e_ezsigntemplatesignature_textvalidation = 'None',
                e_ezsigntemplatesignature_dependencyrequirement = 'AllOf',
                s_ezsigntemplatesignature_positioningpattern = 'Signature',
                i_ezsigntemplatesignature_positioningoffsetx = 200,
                i_ezsigntemplatesignature_positioningoffsety = 200,
                e_ezsigntemplatesignature_positioningoccurence = 'All'
            )
        else:
            return EzsigntemplatesignatureRequest(
                fki_ezsigntemplatedocument_id = 133,
                fki_ezsigntemplatesigner_id = 9,
                i_ezsigntemplatedocumentpage_pagenumber = 1,
                i_ezsigntemplatesignature_step = 1,
                e_ezsigntemplatesignature_type = 'Name',
        )
        """

    def testEzsigntemplatesignatureRequest(self):
        """Test EzsigntemplatesignatureRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
