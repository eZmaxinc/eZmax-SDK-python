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

from eZmaxApi.models.country_get_autocomplete_v2_response_m_payload import CountryGetAutocompleteV2ResponseMPayload

class TestCountryGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """CountryGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CountryGetAutocompleteV2ResponseMPayload:
        """Test CountryGetAutocompleteV2ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CountryGetAutocompleteV2ResponseMPayload`
        """
        model = CountryGetAutocompleteV2ResponseMPayload()
        if include_optional:
            return CountryGetAutocompleteV2ResponseMPayload(
                a_obj_country = [
                    eZmaxApi.models.country_autocomplete_element_response.country-AutocompleteElement-Response(
                        pki_country_id = 1, 
                        s_country_name_x = 'Canada', 
                        s_country_shortname = 'CA', 
                        b_country_isactive = True, )
                    ]
            )
        else:
            return CountryGetAutocompleteV2ResponseMPayload(
                a_obj_country = [
                    eZmaxApi.models.country_autocomplete_element_response.country-AutocompleteElement-Response(
                        pki_country_id = 1, 
                        s_country_name_x = 'Canada', 
                        s_country_shortname = 'CA', 
                        b_country_isactive = True, )
                    ],
        )
        """

    def testCountryGetAutocompleteV2ResponseMPayload(self):
        """Test CountryGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
