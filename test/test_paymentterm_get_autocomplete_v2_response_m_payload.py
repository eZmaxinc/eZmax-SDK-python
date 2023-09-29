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

from eZmaxApi.models.paymentterm_get_autocomplete_v2_response_m_payload import PaymenttermGetAutocompleteV2ResponseMPayload  # noqa: E501

class TestPaymenttermGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """PaymenttermGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymenttermGetAutocompleteV2ResponseMPayload:
        """Test PaymenttermGetAutocompleteV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymenttermGetAutocompleteV2ResponseMPayload`
        """
        model = PaymenttermGetAutocompleteV2ResponseMPayload()  # noqa: E501
        if include_optional:
            return PaymenttermGetAutocompleteV2ResponseMPayload(
                a_obj_paymentterm = [
                    eZmaxApi.models.paymentterm_autocomplete_element_response.paymentterm-AutocompleteElement-Response(
                        pki_paymentterm_id = 46, 
                        s_paymentterm_description_x = 'Net 30 days', 
                        b_paymentterm_isactive = True, )
                    ]
            )
        else:
            return PaymenttermGetAutocompleteV2ResponseMPayload(
        )
        """

    def testPaymenttermGetAutocompleteV2ResponseMPayload(self):
        """Test PaymenttermGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()