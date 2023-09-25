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

from eZmaxApi.models.contactinformations_request_compound import ContactinformationsRequestCompound  # noqa: E501

class TestContactinformationsRequestCompound(unittest.TestCase):
    """ContactinformationsRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContactinformationsRequestCompound:
        """Test ContactinformationsRequestCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContactinformationsRequestCompound`
        """
        model = ContactinformationsRequestCompound()  # noqa: E501
        if include_optional:
            return ContactinformationsRequestCompound(
                i_address_default = 56,
                i_phone_default = 56,
                i_email_default = 56,
                i_website_default = 56,
                a_obj_address = [
                    eZmaxApi.models.address_request_compound.address-RequestCompound()
                    ],
                a_obj_phone = [
                    eZmaxApi.models.phone_request_compound.phone-RequestCompound()
                    ],
                a_obj_email = [
                    eZmaxApi.models.email_request_compound.email-RequestCompound()
                    ],
                a_obj_website = [
                    eZmaxApi.models.website_request_compound.website-RequestCompound()
                    ]
            )
        else:
            return ContactinformationsRequestCompound(
                i_address_default = 56,
                i_phone_default = 56,
                i_email_default = 56,
                i_website_default = 56,
                a_obj_address = [
                    eZmaxApi.models.address_request_compound.address-RequestCompound()
                    ],
                a_obj_phone = [
                    eZmaxApi.models.phone_request_compound.phone-RequestCompound()
                    ],
                a_obj_email = [
                    eZmaxApi.models.email_request_compound.email-RequestCompound()
                    ],
                a_obj_website = [
                    eZmaxApi.models.website_request_compound.website-RequestCompound()
                    ],
        )
        """

    def testContactinformationsRequestCompound(self):
        """Test ContactinformationsRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
