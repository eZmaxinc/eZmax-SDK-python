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

from eZmaxApi.models.billingentityinternal_get_autocomplete_v2_response_m_payload import BillingentityinternalGetAutocompleteV2ResponseMPayload

class TestBillingentityinternalGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """BillingentityinternalGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingentityinternalGetAutocompleteV2ResponseMPayload:
        """Test BillingentityinternalGetAutocompleteV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingentityinternalGetAutocompleteV2ResponseMPayload`
        """
        model = BillingentityinternalGetAutocompleteV2ResponseMPayload()
        if include_optional:
            return BillingentityinternalGetAutocompleteV2ResponseMPayload(
                a_obj_billingentityinternal = [
                    eZmaxApi.models.billingentityinternal_autocomplete_element_response.billingentityinternal-AutocompleteElement-Response(
                        pki_billingentityinternal_id = 1, 
                        s_billingentityinternal_description_x = 'Default', 
                        b_billingentityinternal_isactive = True, )
                    ]
            )
        else:
            return BillingentityinternalGetAutocompleteV2ResponseMPayload(
                a_obj_billingentityinternal = [
                    eZmaxApi.models.billingentityinternal_autocomplete_element_response.billingentityinternal-AutocompleteElement-Response(
                        pki_billingentityinternal_id = 1, 
                        s_billingentityinternal_description_x = 'Default', 
                        b_billingentityinternal_isactive = True, )
                    ],
        )
        """

    def testBillingentityinternalGetAutocompleteV2ResponseMPayload(self):
        """Test BillingentityinternalGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
