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

from eZmaxApi.models.ezmaxproduct_get_autocomplete_v2_response_m_payload import EzmaxproductGetAutocompleteV2ResponseMPayload

class TestEzmaxproductGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """EzmaxproductGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzmaxproductGetAutocompleteV2ResponseMPayload:
        """Test EzmaxproductGetAutocompleteV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzmaxproductGetAutocompleteV2ResponseMPayload`
        """
        model = EzmaxproductGetAutocompleteV2ResponseMPayload()
        if include_optional:
            return EzmaxproductGetAutocompleteV2ResponseMPayload(
                a_obj_ezmaxproduct = [
                    eZmaxApi.models.ezmaxproduct_autocomplete_element_response.ezmaxproduct-AutocompleteElement-Response(
                        pki_ezmaxproduct_id = 172, 
                        s_ezmaxproduct_description_x = 'eZmax (License)', 
                        b_ezmaxproduct_isactive = True, )
                    ]
            )
        else:
            return EzmaxproductGetAutocompleteV2ResponseMPayload(
                a_obj_ezmaxproduct = [
                    eZmaxApi.models.ezmaxproduct_autocomplete_element_response.ezmaxproduct-AutocompleteElement-Response(
                        pki_ezmaxproduct_id = 172, 
                        s_ezmaxproduct_description_x = 'eZmax (License)', 
                        b_ezmaxproduct_isactive = True, )
                    ],
        )
        """

    def testEzmaxproductGetAutocompleteV2ResponseMPayload(self):
        """Test EzmaxproductGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
