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

from eZmaxApi.models.scim_authentication_scheme import ScimAuthenticationScheme

class TestScimAuthenticationScheme(unittest.TestCase):
    """ScimAuthenticationScheme unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScimAuthenticationScheme:
        """Test ScimAuthenticationScheme
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScimAuthenticationScheme`
        """
        model = ScimAuthenticationScheme()
        if include_optional:
            return ScimAuthenticationScheme(
                description = 'Bearer token in the Authorization header',
                name = 'Bearer',
                type = 'oauthbearertoken'
            )
        else:
            return ScimAuthenticationScheme(
                description = 'Bearer token in the Authorization header',
                name = 'Bearer',
                type = 'oauthbearertoken',
        )
        """

    def testScimAuthenticationScheme(self):
        """Test ScimAuthenticationScheme"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
