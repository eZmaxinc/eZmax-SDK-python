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

from eZmaxApi.models.usergroup_autocomplete_element_response import UsergroupAutocompleteElementResponse  # noqa: E501

class TestUsergroupAutocompleteElementResponse(unittest.TestCase):
    """UsergroupAutocompleteElementResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsergroupAutocompleteElementResponse:
        """Test UsergroupAutocompleteElementResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsergroupAutocompleteElementResponse`
        """
        model = UsergroupAutocompleteElementResponse()  # noqa: E501
        if include_optional:
            return UsergroupAutocompleteElementResponse(
                s_usergroup_name_x = 'Administration',
                pki_usergroup_id = 2,
                b_usergroup_isactive = True
            )
        else:
            return UsergroupAutocompleteElementResponse(
                s_usergroup_name_x = 'Administration',
                pki_usergroup_id = 2,
                b_usergroup_isactive = True,
        )
        """

    def testUsergroupAutocompleteElementResponse(self):
        """Test UsergroupAutocompleteElementResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
