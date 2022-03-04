"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.7
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.address_request_compound import AddressRequestCompound
from eZmaxApi.model.contactinformations_request import ContactinformationsRequest
from eZmaxApi.model.contactinformations_request_compound_all_of import ContactinformationsRequestCompoundAllOf
from eZmaxApi.model.email_request_compound import EmailRequestCompound
from eZmaxApi.model.phone_request_compound import PhoneRequestCompound
from eZmaxApi.model.website_request_compound import WebsiteRequestCompound
globals()['AddressRequestCompound'] = AddressRequestCompound
globals()['ContactinformationsRequest'] = ContactinformationsRequest
globals()['ContactinformationsRequestCompoundAllOf'] = ContactinformationsRequestCompoundAllOf
globals()['EmailRequestCompound'] = EmailRequestCompound
globals()['PhoneRequestCompound'] = PhoneRequestCompound
globals()['WebsiteRequestCompound'] = WebsiteRequestCompound
from eZmaxApi.model.contactinformations_request_compound import ContactinformationsRequestCompound


class TestContactinformationsRequestCompound(unittest.TestCase):
    """ContactinformationsRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testContactinformationsRequestCompound(self):
        """Test ContactinformationsRequestCompound"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ContactinformationsRequestCompound()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
