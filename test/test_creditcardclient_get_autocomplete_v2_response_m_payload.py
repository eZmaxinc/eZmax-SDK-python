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

from eZmaxApi.models.creditcardclient_get_autocomplete_v2_response_m_payload import CreditcardclientGetAutocompleteV2ResponseMPayload

class TestCreditcardclientGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """CreditcardclientGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreditcardclientGetAutocompleteV2ResponseMPayload:
        """Test CreditcardclientGetAutocompleteV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreditcardclientGetAutocompleteV2ResponseMPayload`
        """
        model = CreditcardclientGetAutocompleteV2ResponseMPayload()
        if include_optional:
            return CreditcardclientGetAutocompleteV2ResponseMPayload(
                a_obj_creditcardclient = [
                    eZmaxApi.models.creditcardclient_autocomplete_element_response.creditcardclient-AutocompleteElement-Response(
                        pki_creditcardclient_id = 114, 
                        s_creditcardclient_description = 'Visa', 
                        b_creditcardclient_isactive = True, )
                    ]
            )
        else:
            return CreditcardclientGetAutocompleteV2ResponseMPayload(
                a_obj_creditcardclient = [
                    eZmaxApi.models.creditcardclient_autocomplete_element_response.creditcardclient-AutocompleteElement-Response(
                        pki_creditcardclient_id = 114, 
                        s_creditcardclient_description = 'Visa', 
                        b_creditcardclient_isactive = True, )
                    ],
        )
        """

    def testCreditcardclientGetAutocompleteV2ResponseMPayload(self):
        """Test CreditcardclientGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
