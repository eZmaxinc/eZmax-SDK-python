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

from eZmaxApi.models.module_get_autocomplete_v2_response import ModuleGetAutocompleteV2Response

class TestModuleGetAutocompleteV2Response(unittest.TestCase):
    """ModuleGetAutocompleteV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModuleGetAutocompleteV2Response:
        """Test ModuleGetAutocompleteV2Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModuleGetAutocompleteV2Response`
        """
        model = ModuleGetAutocompleteV2Response()
        if include_optional:
            return ModuleGetAutocompleteV2Response(
                m_payload = eZmaxApi.models.module_get_autocomplete_v2_response_m_payload.module-getAutocomplete-v2-Response-mPayload(
                    a_obj_module = [
                        eZmaxApi.models.module_autocomplete_element_response.module-AutocompleteElement-Response(
                            pki_module_id = 40, 
                            s_module_name_x = 'Purchase', 
                            b_module_isactive = True, )
                        ], )
            )
        else:
            return ModuleGetAutocompleteV2Response(
                m_payload = eZmaxApi.models.module_get_autocomplete_v2_response_m_payload.module-getAutocomplete-v2-Response-mPayload(
                    a_obj_module = [
                        eZmaxApi.models.module_autocomplete_element_response.module-AutocompleteElement-Response(
                            pki_module_id = 40, 
                            s_module_name_x = 'Purchase', 
                            b_module_isactive = True, )
                        ], ),
        )
        """

    def testModuleGetAutocompleteV2Response(self):
        """Test ModuleGetAutocompleteV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
