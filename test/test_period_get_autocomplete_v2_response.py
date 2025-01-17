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

from eZmaxApi.models.period_get_autocomplete_v2_response import PeriodGetAutocompleteV2Response

class TestPeriodGetAutocompleteV2Response(unittest.TestCase):
    """PeriodGetAutocompleteV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PeriodGetAutocompleteV2Response:
        """Test PeriodGetAutocompleteV2Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PeriodGetAutocompleteV2Response`
        """
        model = PeriodGetAutocompleteV2Response()
        if include_optional:
            return PeriodGetAutocompleteV2Response(
                m_payload = eZmaxApi.models.period_get_autocomplete_v2_response_m_payload.period-getAutocomplete-v2-Response-mPayload(
                    a_obj_period = [
                        eZmaxApi.models.period_autocomplete_element_response.period-AutocompleteElement-Response(
                            s_period_yyyymm = '2202-12', 
                            pki_period_id = 21, 
                            b_period_isactive = True, )
                        ], )
            )
        else:
            return PeriodGetAutocompleteV2Response(
                m_payload = eZmaxApi.models.period_get_autocomplete_v2_response_m_payload.period-getAutocomplete-v2-Response-mPayload(
                    a_obj_period = [
                        eZmaxApi.models.period_autocomplete_element_response.period-AutocompleteElement-Response(
                            s_period_yyyymm = '2202-12', 
                            pki_period_id = 21, 
                            b_period_isactive = True, )
                        ], ),
        )
        """

    def testPeriodGetAutocompleteV2Response(self):
        """Test PeriodGetAutocompleteV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
