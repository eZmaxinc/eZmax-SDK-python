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

from eZmaxApi.models.billingentityexternal_get_autocomplete_v2_response import BillingentityexternalGetAutocompleteV2Response

class TestBillingentityexternalGetAutocompleteV2Response(unittest.TestCase):
    """BillingentityexternalGetAutocompleteV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingentityexternalGetAutocompleteV2Response:
        """Test BillingentityexternalGetAutocompleteV2Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingentityexternalGetAutocompleteV2Response`
        """
        model = BillingentityexternalGetAutocompleteV2Response()
        if include_optional:
            return BillingentityexternalGetAutocompleteV2Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, 
                    dt_response_date = '2020-12-31 23:59:59', ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.billingentityexternal_get_autocomplete_v2_response_m_payload.billingentityexternal-getAutocomplete-v2-Response-mPayload(
                    a_obj_billingentityexternal = [
                        eZmaxApi.models.billingentityexternal_autocomplete_element_response.billingentityexternal-AutocompleteElement-Response(
                            pki_billingentityexternal_id = 83, 
                            s_billingentityexternal_description = 'ACME Inc', 
                            b_billingentityexternal_isactive = True, )
                        ], )
            )
        else:
            return BillingentityexternalGetAutocompleteV2Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, 
                    dt_response_date = '2020-12-31 23:59:59', ),
                m_payload = eZmaxApi.models.billingentityexternal_get_autocomplete_v2_response_m_payload.billingentityexternal-getAutocomplete-v2-Response-mPayload(
                    a_obj_billingentityexternal = [
                        eZmaxApi.models.billingentityexternal_autocomplete_element_response.billingentityexternal-AutocompleteElement-Response(
                            pki_billingentityexternal_id = 83, 
                            s_billingentityexternal_description = 'ACME Inc', 
                            b_billingentityexternal_isactive = True, )
                        ], ),
        )
        """

    def testBillingentityexternalGetAutocompleteV2Response(self):
        """Test BillingentityexternalGetAutocompleteV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
