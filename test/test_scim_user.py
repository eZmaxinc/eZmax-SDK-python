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

from eZmaxApi.models.scim_user import ScimUser  # noqa: E501

class TestScimUser(unittest.TestCase):
    """ScimUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScimUser:
        """Test ScimUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScimUser`
        """
        model = ScimUser()  # noqa: E501
        if include_optional:
            return ScimUser(
                id = '',
                user_name = '',
                display_name = '',
                emails = [
                    eZmaxApi.models.scim_email.Scim-Email(
                        value = 'email@example.com', 
                        primary = True, )
                    ]
            )
        else:
            return ScimUser(
                user_name = '',
        )
        """

    def testScimUser(self):
        """Test ScimUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()