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

from eZmaxApi.models.language_get_autocomplete_v2_response_m_payload import LanguageGetAutocompleteV2ResponseMPayload

class TestLanguageGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """LanguageGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LanguageGetAutocompleteV2ResponseMPayload:
        """Test LanguageGetAutocompleteV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LanguageGetAutocompleteV2ResponseMPayload`
        """
        model = LanguageGetAutocompleteV2ResponseMPayload()
        if include_optional:
            return LanguageGetAutocompleteV2ResponseMPayload(
                a_obj_language = [
                    eZmaxApi.models.language_autocomplete_element_response.language-AutocompleteElement-Response(
                        pki_language_id = 2, 
                        s_language_name_x = 'English', 
                        b_language_isactive = True, )
                    ]
            )
        else:
            return LanguageGetAutocompleteV2ResponseMPayload(
                a_obj_language = [
                    eZmaxApi.models.language_autocomplete_element_response.language-AutocompleteElement-Response(
                        pki_language_id = 2, 
                        s_language_name_x = 'English', 
                        b_language_isactive = True, )
                    ],
        )
        """

    def testLanguageGetAutocompleteV2ResponseMPayload(self):
        """Test LanguageGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
