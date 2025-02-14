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

from eZmaxApi.models.user_get_autocomplete_v2_response_m_payload import UserGetAutocompleteV2ResponseMPayload

class TestUserGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """UserGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserGetAutocompleteV2ResponseMPayload:
        """Test UserGetAutocompleteV2ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserGetAutocompleteV2ResponseMPayload`
        """
        model = UserGetAutocompleteV2ResponseMPayload()
        if include_optional:
            return UserGetAutocompleteV2ResponseMPayload(
                a_obj_user = [
                    eZmaxApi.models.user_autocomplete_element_response.user-AutocompleteElement-Response(
                        e_user_type = 'EzsignUser', 
                        s_user_name = 'Default', 
                        pki_user_id = 70, 
                        b_user_isactive = True, )
                    ]
            )
        else:
            return UserGetAutocompleteV2ResponseMPayload(
                a_obj_user = [
                    eZmaxApi.models.user_autocomplete_element_response.user-AutocompleteElement-Response(
                        e_user_type = 'EzsignUser', 
                        s_user_name = 'Default', 
                        pki_user_id = 70, 
                        b_user_isactive = True, )
                    ],
        )
        """

    def testUserGetAutocompleteV2ResponseMPayload(self):
        """Test UserGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
