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

from eZmaxApi.models.creditcardtype_get_autocomplete_v2_response_m_payload import CreditcardtypeGetAutocompleteV2ResponseMPayload

class TestCreditcardtypeGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """CreditcardtypeGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreditcardtypeGetAutocompleteV2ResponseMPayload:
        """Test CreditcardtypeGetAutocompleteV2ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreditcardtypeGetAutocompleteV2ResponseMPayload`
        """
        model = CreditcardtypeGetAutocompleteV2ResponseMPayload()
        if include_optional:
            return CreditcardtypeGetAutocompleteV2ResponseMPayload(
                a_obj_creditcardtype = [
                    eZmaxApi.models.creditcardtype_autocomplete_element_response.creditcardtype-AutocompleteElement-Response(
                        s_creditcardtype_name = 'Visa', 
                        pki_creditcardtype_id = 2, 
                        e_creditcardtype_codename = 'visa', )
                    ]
            )
        else:
            return CreditcardtypeGetAutocompleteV2ResponseMPayload(
                a_obj_creditcardtype = [
                    eZmaxApi.models.creditcardtype_autocomplete_element_response.creditcardtype-AutocompleteElement-Response(
                        s_creditcardtype_name = 'Visa', 
                        pki_creditcardtype_id = 2, 
                        e_creditcardtype_codename = 'visa', )
                    ],
        )
        """

    def testCreditcardtypeGetAutocompleteV2ResponseMPayload(self):
        """Test CreditcardtypeGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
