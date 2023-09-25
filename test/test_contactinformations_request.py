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

from eZmaxApi.models.contactinformations_request import ContactinformationsRequest  # noqa: E501

class TestContactinformationsRequest(unittest.TestCase):
    """ContactinformationsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContactinformationsRequest:
        """Test ContactinformationsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContactinformationsRequest`
        """
        model = ContactinformationsRequest()  # noqa: E501
        if include_optional:
            return ContactinformationsRequest(
                i_address_default = 56,
                i_phone_default = 56,
                i_email_default = 56,
                i_website_default = 56
            )
        else:
            return ContactinformationsRequest(
                i_address_default = 56,
                i_phone_default = 56,
                i_email_default = 56,
                i_website_default = 56,
        )
        """

    def testContactinformationsRequest(self):
        """Test ContactinformationsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
