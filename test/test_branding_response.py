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

from eZmaxApi.models.branding_response import BrandingResponse  # noqa: E501

class TestBrandingResponse(unittest.TestCase):
    """BrandingResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BrandingResponse:
        """Test BrandingResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BrandingResponse`
        """
        model = BrandingResponse()  # noqa: E501
        if include_optional:
            return BrandingResponse(
                pki_branding_id = 78,
                fki_email_id = 22,
                obj_branding_description = eZmaxApi.models.multilingual_branding_description.Multilingual-BrandingDescription(
                    s_branding_description1 = 'Compagnie X', 
                    s_branding_description2 = 'Company X', ),
                s_branding_description_x = 'Company X',
                s_branding_name = 'eZmax (Corp)',
                s_email_address = 'email@example.com',
                e_branding_logo = 'Default',
                i_branding_colortext = 3752795,
                i_branding_colortextlinkbox = 0,
                i_branding_colortextbutton = 16777215,
                i_branding_colorbackground = 15658734,
                i_branding_colorbackgroundbutton = 13577007,
                i_branding_colorbackgroundsmallbox = 16777215,
                b_branding_isactive = True
            )
        else:
            return BrandingResponse(
                pki_branding_id = 78,
                obj_branding_description = eZmaxApi.models.multilingual_branding_description.Multilingual-BrandingDescription(
                    s_branding_description1 = 'Compagnie X', 
                    s_branding_description2 = 'Company X', ),
                s_branding_description_x = 'Company X',
                e_branding_logo = 'Default',
                i_branding_colortext = 3752795,
                i_branding_colortextlinkbox = 0,
                i_branding_colortextbutton = 16777215,
                i_branding_colorbackground = 15658734,
                i_branding_colorbackgroundbutton = 13577007,
                i_branding_colorbackgroundsmallbox = 16777215,
                b_branding_isactive = True,
        )
        """

    def testBrandingResponse(self):
        """Test BrandingResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
