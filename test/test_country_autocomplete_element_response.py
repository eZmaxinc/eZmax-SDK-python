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

from eZmaxApi.models.country_autocomplete_element_response import CountryAutocompleteElementResponse

class TestCountryAutocompleteElementResponse(unittest.TestCase):
    """CountryAutocompleteElementResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CountryAutocompleteElementResponse:
        """Test CountryAutocompleteElementResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CountryAutocompleteElementResponse`
        """
        model = CountryAutocompleteElementResponse()
        if include_optional:
            return CountryAutocompleteElementResponse(
                pki_country_id = 1,
                s_country_name_x = 'Canada',
                s_country_shortname = 'CA',
                b_country_isactive = True
            )
        else:
            return CountryAutocompleteElementResponse(
                pki_country_id = 1,
                s_country_name_x = 'Canada',
                s_country_shortname = 'CA',
                b_country_isactive = True,
        )
        """

    def testCountryAutocompleteElementResponse(self):
        """Test CountryAutocompleteElementResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
