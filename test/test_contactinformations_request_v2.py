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

from eZmaxApi.models.contactinformations_request_v2 import ContactinformationsRequestV2

class TestContactinformationsRequestV2(unittest.TestCase):
    """ContactinformationsRequestV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContactinformationsRequestV2:
        """Test ContactinformationsRequestV2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContactinformationsRequestV2`
        """
        model = ContactinformationsRequestV2()
        if include_optional:
            return ContactinformationsRequestV2(
                e_contactinformations_type = 'BankAccount',
                i_address_default = 56,
                i_phone_default = 56,
                i_email_default = 56,
                i_website_default = 56
            )
        else:
            return ContactinformationsRequestV2(
                e_contactinformations_type = 'BankAccount',
                i_address_default = 56,
                i_phone_default = 56,
                i_email_default = 56,
                i_website_default = 56,
        )
        """

    def testContactinformationsRequestV2(self):
        """Test ContactinformationsRequestV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
