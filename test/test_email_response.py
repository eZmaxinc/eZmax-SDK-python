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

from eZmaxApi.models.email_response import EmailResponse  # noqa: E501

class TestEmailResponse(unittest.TestCase):
    """EmailResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmailResponse:
        """Test EmailResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmailResponse`
        """
        model = EmailResponse()  # noqa: E501
        if include_optional:
            return EmailResponse(
                pki_email_id = 22,
                fki_emailtype_id = 1,
                s_email_address = 'email@example.com'
            )
        else:
            return EmailResponse(
                pki_email_id = 22,
                fki_emailtype_id = 1,
                s_email_address = 'email@example.com',
        )
        """

    def testEmailResponse(self):
        """Test EmailResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()