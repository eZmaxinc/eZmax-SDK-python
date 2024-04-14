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

from eZmaxApi.models.ezsigntemplatepackage_get_autocomplete_v2_response import EzsigntemplatepackageGetAutocompleteV2Response

class TestEzsigntemplatepackageGetAutocompleteV2Response(unittest.TestCase):
    """EzsigntemplatepackageGetAutocompleteV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatepackageGetAutocompleteV2Response:
        """Test EzsigntemplatepackageGetAutocompleteV2Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatepackageGetAutocompleteV2Response`
        """
        model = EzsigntemplatepackageGetAutocompleteV2Response()
        if include_optional:
            return EzsigntemplatepackageGetAutocompleteV2Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, 
                    dt_response_date = '2020-12-31 23:59:59', ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.ezsigntemplatepackage_get_autocomplete_v2_response_m_payload.ezsigntemplatepackage-getAutocomplete-v2-Response-mPayload(
                    a_obj_ezsigntemplatepackage = [
                        eZmaxApi.models.ezsigntemplatepackage_autocomplete_element_response.ezsigntemplatepackage-AutocompleteElement-Response(
                            e_ezsignfoldertype_privacylevel = 'User', 
                            s_ezsigntemplatepackage_description = 'Package for new clients', 
                            pki_ezsigntemplatepackage_id = 99, 
                            b_ezsigntemplatepackage_isactive = True, 
                            b_disabled = True, )
                        ], )
            )
        else:
            return EzsigntemplatepackageGetAutocompleteV2Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, 
                    dt_response_date = '2020-12-31 23:59:59', ),
                m_payload = eZmaxApi.models.ezsigntemplatepackage_get_autocomplete_v2_response_m_payload.ezsigntemplatepackage-getAutocomplete-v2-Response-mPayload(
                    a_obj_ezsigntemplatepackage = [
                        eZmaxApi.models.ezsigntemplatepackage_autocomplete_element_response.ezsigntemplatepackage-AutocompleteElement-Response(
                            e_ezsignfoldertype_privacylevel = 'User', 
                            s_ezsigntemplatepackage_description = 'Package for new clients', 
                            pki_ezsigntemplatepackage_id = 99, 
                            b_ezsigntemplatepackage_isactive = True, 
                            b_disabled = True, )
                        ], ),
        )
        """

    def testEzsigntemplatepackageGetAutocompleteV2Response(self):
        """Test EzsigntemplatepackageGetAutocompleteV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
