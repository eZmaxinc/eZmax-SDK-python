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

from eZmaxApi.models.company_get_autocomplete_v2_response import CompanyGetAutocompleteV2Response

class TestCompanyGetAutocompleteV2Response(unittest.TestCase):
    """CompanyGetAutocompleteV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompanyGetAutocompleteV2Response:
        """Test CompanyGetAutocompleteV2Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompanyGetAutocompleteV2Response`
        """
        model = CompanyGetAutocompleteV2Response()
        if include_optional:
            return CompanyGetAutocompleteV2Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.company_get_autocomplete_v2_response_m_payload.company-getAutocomplete-v2-Response-mPayload(
                    a_obj_company = [
                        eZmaxApi.models.company_autocomplete_element_response.company-AutocompleteElement-Response(
                            pki_company_id = 1, 
                            s_company_name_x = 'Acme inc.', 
                            b_company_isactive = True, )
                        ], )
            )
        else:
            return CompanyGetAutocompleteV2Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                m_payload = eZmaxApi.models.company_get_autocomplete_v2_response_m_payload.company-getAutocomplete-v2-Response-mPayload(
                    a_obj_company = [
                        eZmaxApi.models.company_autocomplete_element_response.company-AutocompleteElement-Response(
                            pki_company_id = 1, 
                            s_company_name_x = 'Acme inc.', 
                            b_company_isactive = True, )
                        ], ),
        )
        """

    def testCompanyGetAutocompleteV2Response(self):
        """Test CompanyGetAutocompleteV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
