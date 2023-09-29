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

from eZmaxApi.models.variableexpense_get_autocomplete_v2_response_m_payload import VariableexpenseGetAutocompleteV2ResponseMPayload  # noqa: E501

class TestVariableexpenseGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """VariableexpenseGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VariableexpenseGetAutocompleteV2ResponseMPayload:
        """Test VariableexpenseGetAutocompleteV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VariableexpenseGetAutocompleteV2ResponseMPayload`
        """
        model = VariableexpenseGetAutocompleteV2ResponseMPayload()  # noqa: E501
        if include_optional:
            return VariableexpenseGetAutocompleteV2ResponseMPayload(
                a_obj_variableexpense = [
                    eZmaxApi.models.variableexpense_autocomplete_element_response.variableexpense-AutocompleteElement-Response(
                        s_variableexpense_description_x = 'Équipements de bureau', 
                        pki_variableexpense_id = 2, 
                        b_variableexpense_isactive = True, )
                    ]
            )
        else:
            return VariableexpenseGetAutocompleteV2ResponseMPayload(
        )
        """

    def testVariableexpenseGetAutocompleteV2ResponseMPayload(self):
        """Test VariableexpenseGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()