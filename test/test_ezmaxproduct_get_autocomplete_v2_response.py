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

from eZmaxApi.models.ezmaxproduct_get_autocomplete_v2_response import EzmaxproductGetAutocompleteV2Response

class TestEzmaxproductGetAutocompleteV2Response(unittest.TestCase):
    """EzmaxproductGetAutocompleteV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzmaxproductGetAutocompleteV2Response:
        """Test EzmaxproductGetAutocompleteV2Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzmaxproductGetAutocompleteV2Response`
        """
        model = EzmaxproductGetAutocompleteV2Response()
        if include_optional:
            return EzmaxproductGetAutocompleteV2Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, 
                    dt_response_date = '2020-12-31 23:59:59', ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.ezmaxproduct_get_autocomplete_v2_response_m_payload.ezmaxproduct-getAutocomplete-v2-Response-mPayload(
                    a_obj_ezmaxproduct = [
                        eZmaxApi.models.ezmaxproduct_autocomplete_element_response.ezmaxproduct-AutocompleteElement-Response(
                            pki_ezmaxproduct_id = 172, 
                            s_ezmaxproduct_description_x = 'eZmax (License)', 
                            b_ezmaxproduct_isactive = True, )
                        ], )
            )
        else:
            return EzmaxproductGetAutocompleteV2Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, 
                    dt_response_date = '2020-12-31 23:59:59', ),
                m_payload = eZmaxApi.models.ezmaxproduct_get_autocomplete_v2_response_m_payload.ezmaxproduct-getAutocomplete-v2-Response-mPayload(
                    a_obj_ezmaxproduct = [
                        eZmaxApi.models.ezmaxproduct_autocomplete_element_response.ezmaxproduct-AutocompleteElement-Response(
                            pki_ezmaxproduct_id = 172, 
                            s_ezmaxproduct_description_x = 'eZmax (License)', 
                            b_ezmaxproduct_isactive = True, )
                        ], ),
        )
        """

    def testEzmaxproductGetAutocompleteV2Response(self):
        """Test EzmaxproductGetAutocompleteV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
