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

from eZmaxApi.models.usergroup_get_autocomplete_v2_response_m_payload import UsergroupGetAutocompleteV2ResponseMPayload

class TestUsergroupGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """UsergroupGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsergroupGetAutocompleteV2ResponseMPayload:
        """Test UsergroupGetAutocompleteV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsergroupGetAutocompleteV2ResponseMPayload`
        """
        model = UsergroupGetAutocompleteV2ResponseMPayload()
        if include_optional:
            return UsergroupGetAutocompleteV2ResponseMPayload(
                a_obj_usergroup = [
                    eZmaxApi.models.usergroup_autocomplete_element_response.usergroup-AutocompleteElement-Response(
                        s_usergroup_name_x = 'Administration', 
                        pki_usergroup_id = 2, 
                        b_usergroup_isactive = True, )
                    ]
            )
        else:
            return UsergroupGetAutocompleteV2ResponseMPayload(
                a_obj_usergroup = [
                    eZmaxApi.models.usergroup_autocomplete_element_response.usergroup-AutocompleteElement-Response(
                        s_usergroup_name_x = 'Administration', 
                        pki_usergroup_id = 2, 
                        b_usergroup_isactive = True, )
                    ],
        )
        """

    def testUsergroupGetAutocompleteV2ResponseMPayload(self):
        """Test UsergroupGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
