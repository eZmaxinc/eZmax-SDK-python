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

from eZmaxApi.models.authenticationexternal_get_autocomplete_v2_response_m_payload import AuthenticationexternalGetAutocompleteV2ResponseMPayload

class TestAuthenticationexternalGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """AuthenticationexternalGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthenticationexternalGetAutocompleteV2ResponseMPayload:
        """Test AuthenticationexternalGetAutocompleteV2ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthenticationexternalGetAutocompleteV2ResponseMPayload`
        """
        model = AuthenticationexternalGetAutocompleteV2ResponseMPayload()
        if include_optional:
            return AuthenticationexternalGetAutocompleteV2ResponseMPayload(
                a_obj_authenticationexternal = [
                    eZmaxApi.models.authenticationexternal_autocomplete_element_response.authenticationexternal-AutocompleteElement-Response(
                        pki_authenticationexternal_id = 56, 
                        s_authenticationexternal_description = 'Authentification', 
                        b_authenticationexternal_isactive = True, )
                    ]
            )
        else:
            return AuthenticationexternalGetAutocompleteV2ResponseMPayload(
                a_obj_authenticationexternal = [
                    eZmaxApi.models.authenticationexternal_autocomplete_element_response.authenticationexternal-AutocompleteElement-Response(
                        pki_authenticationexternal_id = 56, 
                        s_authenticationexternal_description = 'Authentification', 
                        b_authenticationexternal_isactive = True, )
                    ],
        )
        """

    def testAuthenticationexternalGetAutocompleteV2ResponseMPayload(self):
        """Test AuthenticationexternalGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
