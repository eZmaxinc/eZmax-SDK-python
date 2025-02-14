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

from eZmaxApi.models.scim_user_list import ScimUserList

class TestScimUserList(unittest.TestCase):
    """ScimUserList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScimUserList:
        """Test ScimUserList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScimUserList`
        """
        model = ScimUserList()
        if include_optional:
            return ScimUserList(
                total_results = 56,
                items_per_page = 56,
                start_index = 56,
                schemas = [
                    ''
                    ],
                resources = [
                    eZmaxApi.models.scim_user.Scim-User(
                        id = '', 
                        user_name = '', 
                        display_name = '', 
                        emails = [
                            eZmaxApi.models.scim_email.Scim-Email(
                                value = 'email@example.com', 
                                primary = True, )
                            ], )
                    ]
            )
        else:
            return ScimUserList(
        )
        """

    def testScimUserList(self):
        """Test ScimUserList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
