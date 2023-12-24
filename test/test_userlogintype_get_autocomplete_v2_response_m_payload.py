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

from eZmaxApi.models.userlogintype_get_autocomplete_v2_response_m_payload import UserlogintypeGetAutocompleteV2ResponseMPayload

class TestUserlogintypeGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """UserlogintypeGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserlogintypeGetAutocompleteV2ResponseMPayload:
        """Test UserlogintypeGetAutocompleteV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserlogintypeGetAutocompleteV2ResponseMPayload`
        """
        model = UserlogintypeGetAutocompleteV2ResponseMPayload()
        if include_optional:
            return UserlogintypeGetAutocompleteV2ResponseMPayload(
                a_obj_userlogintype = [
                    eZmaxApi.models.userlogintype_autocomplete_element_response.userlogintype-AutocompleteElement-Response(
                        pki_userlogintype_id = 2, 
                        s_userlogintype_description_x = 'Email and phone or SMS', 
                        b_userlogintype_isactive = True, )
                    ]
            )
        else:
            return UserlogintypeGetAutocompleteV2ResponseMPayload(
                a_obj_userlogintype = [
                    eZmaxApi.models.userlogintype_autocomplete_element_response.userlogintype-AutocompleteElement-Response(
                        pki_userlogintype_id = 2, 
                        s_userlogintype_description_x = 'Email and phone or SMS', 
                        b_userlogintype_isactive = True, )
                    ],
        )
        """

    def testUserlogintypeGetAutocompleteV2ResponseMPayload(self):
        """Test UserlogintypeGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
