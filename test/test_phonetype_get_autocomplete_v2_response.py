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

from eZmaxApi.models.phonetype_get_autocomplete_v2_response import PhonetypeGetAutocompleteV2Response

class TestPhonetypeGetAutocompleteV2Response(unittest.TestCase):
    """PhonetypeGetAutocompleteV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PhonetypeGetAutocompleteV2Response:
        """Test PhonetypeGetAutocompleteV2Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PhonetypeGetAutocompleteV2Response`
        """
        model = PhonetypeGetAutocompleteV2Response()
        if include_optional:
            return PhonetypeGetAutocompleteV2Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.phonetype_get_autocomplete_v2_response_m_payload.phonetype-getAutocomplete-v2-Response-mPayload(
                    a_obj_phonetype = [
                        eZmaxApi.models.phonetype_autocomplete_element_response.phonetype-AutocompleteElement-Response(
                            pki_phonetype_id = 1, 
                            s_phonetype_name_x = 'Office', 
                            b_phonetype_isactive = True, )
                        ], )
            )
        else:
            return PhonetypeGetAutocompleteV2Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                m_payload = eZmaxApi.models.phonetype_get_autocomplete_v2_response_m_payload.phonetype-getAutocomplete-v2-Response-mPayload(
                    a_obj_phonetype = [
                        eZmaxApi.models.phonetype_autocomplete_element_response.phonetype-AutocompleteElement-Response(
                            pki_phonetype_id = 1, 
                            s_phonetype_name_x = 'Office', 
                            b_phonetype_isactive = True, )
                        ], ),
        )
        """

    def testPhonetypeGetAutocompleteV2Response(self):
        """Test PhonetypeGetAutocompleteV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
