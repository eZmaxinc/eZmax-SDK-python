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

from eZmaxApi.models.userstaged_response import UserstagedResponse  # noqa: E501

class TestUserstagedResponse(unittest.TestCase):
    """UserstagedResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserstagedResponse:
        """Test UserstagedResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserstagedResponse`
        """
        model = UserstagedResponse()  # noqa: E501
        if include_optional:
            return UserstagedResponse(
                pki_userstaged_id = 90,
                fki_email_id = 22,
                s_email_address = 'email@example.com',
                s_userstaged_firstname = 'Jane',
                s_userstaged_lastname = 'Doe',
                s_userstaged_externalid = 'azuread_6b303ca8-9e34-4c21-9a53-0856342dec5e'
            )
        else:
            return UserstagedResponse(
                pki_userstaged_id = 90,
                fki_email_id = 22,
                s_email_address = 'email@example.com',
                s_userstaged_firstname = 'Jane',
                s_userstaged_lastname = 'Doe',
                s_userstaged_externalid = 'azuread_6b303ca8-9e34-4c21-9a53-0856342dec5e',
        )
        """

    def testUserstagedResponse(self):
        """Test UserstagedResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
