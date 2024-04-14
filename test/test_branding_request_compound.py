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

from eZmaxApi.models.branding_request_compound import BrandingRequestCompound

class TestBrandingRequestCompound(unittest.TestCase):
    """BrandingRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BrandingRequestCompound:
        """Test BrandingRequestCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BrandingRequestCompound`
        """
        model = BrandingRequestCompound()
        if include_optional:
            return BrandingRequestCompound(
                pki_branding_id = 78,
                obj_branding_description = eZmaxApi.models.multilingual_branding_description.Multilingual-BrandingDescription(
                    s_branding_description1 = 'Compagnie X', 
                    s_branding_description2 = 'Company X', ),
                e_branding_logo = 'Default',
                s_branding_base64 = 'eyIkcmVmIjoiIy9jb21wb25lbnRzL2V4YW1wbGVzL1BuZ0FzQmFzZTY0L3ZhbHVlIn0=',
                e_branding_logointerface = 'Default',
                s_branding_logointerface_base64 = 'eyIkcmVmIjoiIy9jb21wb25lbnRzL2V4YW1wbGVzL1BuZ0FzQmFzZTY0L3ZhbHVlIn0=',
                i_branding_colortext = 3752795,
                i_branding_colortextlinkbox = 0,
                i_branding_colortextbutton = 16777215,
                i_branding_colorbackground = 15658734,
                i_branding_colorbackgroundbutton = 13577007,
                i_branding_colorbackgroundsmallbox = 16777215,
                i_branding_interfacecolor = 15658734,
                s_branding_name = 'eZmax (Corp)',
                s_email_address = 'email@example.com',
                b_branding_isactive = True
            )
        else:
            return BrandingRequestCompound(
                obj_branding_description = eZmaxApi.models.multilingual_branding_description.Multilingual-BrandingDescription(
                    s_branding_description1 = 'Compagnie X', 
                    s_branding_description2 = 'Company X', ),
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

    def testBrandingRequestCompound(self):
        """Test BrandingRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
