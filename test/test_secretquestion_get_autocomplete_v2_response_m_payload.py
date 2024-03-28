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

from eZmaxApi.models.secretquestion_get_autocomplete_v2_response_m_payload import SecretquestionGetAutocompleteV2ResponseMPayload

class TestSecretquestionGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """SecretquestionGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SecretquestionGetAutocompleteV2ResponseMPayload:
        """Test SecretquestionGetAutocompleteV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SecretquestionGetAutocompleteV2ResponseMPayload`
        """
        model = SecretquestionGetAutocompleteV2ResponseMPayload()
        if include_optional:
            return SecretquestionGetAutocompleteV2ResponseMPayload(
                a_obj_secretquestion = [
                    eZmaxApi.models.secretquestion_autocomplete_element_response.secretquestion-AutocompleteElement-Response(
                        s_secretquestion_text_x = 'The name of the hospital in which you were born', 
                        pki_secretquestion_id = 7, 
                        b_secretquestion_isactive = True, )
                    ]
            )
        else:
            return SecretquestionGetAutocompleteV2ResponseMPayload(
                a_obj_secretquestion = [
                    eZmaxApi.models.secretquestion_autocomplete_element_response.secretquestion-AutocompleteElement-Response(
                        s_secretquestion_text_x = 'The name of the hospital in which you were born', 
                        pki_secretquestion_id = 7, 
                        b_secretquestion_isactive = True, )
                    ],
        )
        """

    def testSecretquestionGetAutocompleteV2ResponseMPayload(self):
        """Test SecretquestionGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
