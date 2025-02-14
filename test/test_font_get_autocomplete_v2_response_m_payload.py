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

from eZmaxApi.models.font_get_autocomplete_v2_response_m_payload import FontGetAutocompleteV2ResponseMPayload

class TestFontGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """FontGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FontGetAutocompleteV2ResponseMPayload:
        """Test FontGetAutocompleteV2ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FontGetAutocompleteV2ResponseMPayload`
        """
        model = FontGetAutocompleteV2ResponseMPayload()
        if include_optional:
            return FontGetAutocompleteV2ResponseMPayload(
                a_obj_font = [
                    eZmaxApi.models.font_autocomplete_element_response.font-AutocompleteElement-Response(
                        s_font_name = 'Arial', 
                        pki_font_id = 1, 
                        b_font_isactive = True, )
                    ]
            )
        else:
            return FontGetAutocompleteV2ResponseMPayload(
                a_obj_font = [
                    eZmaxApi.models.font_autocomplete_element_response.font-AutocompleteElement-Response(
                        s_font_name = 'Arial', 
                        pki_font_id = 1, 
                        b_font_isactive = True, )
                    ],
        )
        """

    def testFontGetAutocompleteV2ResponseMPayload(self):
        """Test FontGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
