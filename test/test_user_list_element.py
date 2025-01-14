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

from eZmaxApi.models.user_list_element import UserListElement

class TestUserListElement(unittest.TestCase):
    """UserListElement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserListElement:
        """Test UserListElement
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserListElement`
        """
        model = UserListElement()
        if include_optional:
            return UserListElement(
                pki_user_id = 70,
                s_user_firstname = 'John',
                s_user_lastname = 'Doe',
                s_user_loginname = 'JohnDoe',
                b_user_isactive = True,
                e_user_type = 'EzsignUser',
                e_user_origin = 'BuiltIn',
                e_user_ezsignaccess = 'PaidByOffice',
                dt_user_ezsignprepaidexpiration = '2020-12-31',
                s_email_address = 'email@example.com',
                s_user_jobtitle = 'Sales Representative'
            )
        else:
            return UserListElement(
                pki_user_id = 70,
                s_user_firstname = 'John',
                s_user_lastname = 'Doe',
                s_user_loginname = 'JohnDoe',
                b_user_isactive = True,
                e_user_type = 'EzsignUser',
                e_user_origin = 'BuiltIn',
                e_user_ezsignaccess = 'PaidByOffice',
                s_email_address = 'email@example.com',
        )
        """

    def testUserListElement(self):
        """Test UserListElement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
