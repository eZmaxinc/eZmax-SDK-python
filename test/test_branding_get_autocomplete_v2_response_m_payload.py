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

from eZmaxApi.models.branding_get_autocomplete_v2_response_m_payload import BrandingGetAutocompleteV2ResponseMPayload

class TestBrandingGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """BrandingGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BrandingGetAutocompleteV2ResponseMPayload:
        """Test BrandingGetAutocompleteV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BrandingGetAutocompleteV2ResponseMPayload`
        """
        model = BrandingGetAutocompleteV2ResponseMPayload()
        if include_optional:
            return BrandingGetAutocompleteV2ResponseMPayload(
                a_obj_branding = [
                    eZmaxApi.models.branding_autocomplete_element_response.branding-AutocompleteElement-Response(
                        s_branding_description_x = 'Company X', 
                        pki_branding_id = 78, 
                        b_branding_isactive = True, )
                    ]
            )
        else:
            return BrandingGetAutocompleteV2ResponseMPayload(
                a_obj_branding = [
                    eZmaxApi.models.branding_autocomplete_element_response.branding-AutocompleteElement-Response(
                        s_branding_description_x = 'Company X', 
                        pki_branding_id = 78, 
                        b_branding_isactive = True, )
                    ],
        )
        """

    def testBrandingGetAutocompleteV2ResponseMPayload(self):
        """Test BrandingGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
