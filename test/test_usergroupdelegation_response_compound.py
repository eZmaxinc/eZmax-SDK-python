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

from eZmaxApi.models.usergroupdelegation_response_compound import UsergroupdelegationResponseCompound  # noqa: E501

class TestUsergroupdelegationResponseCompound(unittest.TestCase):
    """UsergroupdelegationResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsergroupdelegationResponseCompound:
        """Test UsergroupdelegationResponseCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsergroupdelegationResponseCompound`
        """
        model = UsergroupdelegationResponseCompound()  # noqa: E501
        if include_optional:
            return UsergroupdelegationResponseCompound(
                pki_usergroupdelegation_id = 141,
                fki_usergroup_id = 2,
                fki_user_id = 70,
                s_user_firstname = 'John',
                s_user_lastname = 'Doe',
                s_user_loginname = 'JohnDoe',
                s_email_address = 'email@example.com',
                s_usergroup_name_x = 'Administration'
            )
        else:
            return UsergroupdelegationResponseCompound(
                pki_usergroupdelegation_id = 141,
                fki_usergroup_id = 2,
                fki_user_id = 70,
                s_user_firstname = 'John',
                s_user_lastname = 'Doe',
                s_user_loginname = 'JohnDoe',
                s_usergroup_name_x = 'Administration',
        )
        """

    def testUsergroupdelegationResponseCompound(self):
        """Test UsergroupdelegationResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
