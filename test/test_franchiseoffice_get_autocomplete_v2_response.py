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

from eZmaxApi.models.franchiseoffice_get_autocomplete_v2_response import FranchiseofficeGetAutocompleteV2Response

class TestFranchiseofficeGetAutocompleteV2Response(unittest.TestCase):
    """FranchiseofficeGetAutocompleteV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FranchiseofficeGetAutocompleteV2Response:
        """Test FranchiseofficeGetAutocompleteV2Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FranchiseofficeGetAutocompleteV2Response`
        """
        model = FranchiseofficeGetAutocompleteV2Response()
        if include_optional:
            return FranchiseofficeGetAutocompleteV2Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.franchiseoffice_get_autocomplete_v2_response_m_payload.franchiseoffice-getAutocomplete-v2-Response-mPayload(
                    a_obj_franchiseoffice = [
                        eZmaxApi.models.franchiseoffice_autocomplete_element_response.franchiseoffice-AutocompleteElement-Response(
                            s_franchiseoffice_description = 'Default', 
                            pki_franchiseoffice_id = 50, 
                            b_franchiseoffice_isactive = True, )
                        ], )
            )
        else:
            return FranchiseofficeGetAutocompleteV2Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                m_payload = eZmaxApi.models.franchiseoffice_get_autocomplete_v2_response_m_payload.franchiseoffice-getAutocomplete-v2-Response-mPayload(
                    a_obj_franchiseoffice = [
                        eZmaxApi.models.franchiseoffice_autocomplete_element_response.franchiseoffice-AutocompleteElement-Response(
                            s_franchiseoffice_description = 'Default', 
                            pki_franchiseoffice_id = 50, 
                            b_franchiseoffice_isactive = True, )
                        ], ),
        )
        """

    def testFranchiseofficeGetAutocompleteV2Response(self):
        """Test FranchiseofficeGetAutocompleteV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
