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

from eZmaxApi.models.scim_email import ScimEmail

class TestScimEmail(unittest.TestCase):
    """ScimEmail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScimEmail:
        """Test ScimEmail
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScimEmail`
        """
        model = ScimEmail()
        if include_optional:
            return ScimEmail(
                value = 'email@example.com',
                primary = True
            )
        else:
            return ScimEmail(
        )
        """

    def testScimEmail(self):
        """Test ScimEmail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
