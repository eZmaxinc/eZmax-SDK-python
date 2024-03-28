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

from eZmaxApi.models.ezsignsignature_request_compound import EzsignsignatureRequestCompound

class TestEzsignsignatureRequestCompound(unittest.TestCase):
    """EzsignsignatureRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignatureRequestCompound:
        """Test EzsignsignatureRequestCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignatureRequestCompound`
        """
        model = EzsignsignatureRequestCompound()
        if include_optional:
            return EzsignsignatureRequestCompound(
                pki_ezsignsignature_id = 49,
                fki_ezsignfoldersignerassociation_id = 20,
                i_ezsignpage_pagenumber = 1,
                i_ezsignsignature_x = 200,
                i_ezsignsignature_y = 300,
                i_ezsignsignature_width = 200,
                i_ezsignsignature_height = 200,
                i_ezsignsignature_step = 1,
                e_ezsignsignature_type = 'Name',
                fki_ezsigndocument_id = 97,
                t_ezsignsignature_tooltip = 'Please sign here if you agree to the terms',
                e_ezsignsignature_tooltipposition = 'TopLeft',
                e_ezsignsignature_font = 'Normal',
                fki_ezsignfoldersignerassociation_id_validation = 20,
                b_ezsignsignature_required = True,
                e_ezsignsignature_attachmentnamesource = 'Description',
                s_ezsignsignature_attachmentdescription = 'Attachment',
                i_ezsignsignature_validationstep = 1,
                i_ezsignsignature_maxlength = 75,
                e_ezsignsignature_textvalidation = 'None',
                s_ezsignsignature_regexp = '/[-0-9a-zA-Z.+_]+@[-0-9a-zA-Z.+_]+.[a-zA-Z]{2,4}/',
                e_ezsignsignature_dependencyrequirement = 'AllOf',
                b_ezsignsignature_customdate = True,
                a_obj_ezsignsignaturecustomdate = [
                    eZmaxApi.models.ezsignsignaturecustomdate_request_compound.ezsignsignaturecustomdate-RequestCompound()
                    ],
                a_obj_ezsignelementdependency = [
                    eZmaxApi.models.ezsignelementdependency_request_compound.ezsignelementdependency-RequestCompound()
                    ]
            )
        else:
            return EzsignsignatureRequestCompound(
                fki_ezsignfoldersignerassociation_id = 20,
                i_ezsignpage_pagenumber = 1,
                i_ezsignsignature_x = 200,
                i_ezsignsignature_y = 300,
                i_ezsignsignature_step = 1,
                e_ezsignsignature_type = 'Name',
                fki_ezsigndocument_id = 97,
        )
        """

    def testEzsignsignatureRequestCompound(self):
        """Test EzsignsignatureRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
