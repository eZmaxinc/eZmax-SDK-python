"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.4
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.address_request import AddressRequest
from eZmaxApi.model.email_request import EmailRequest
from eZmaxApi.model.phone_request import PhoneRequest
from eZmaxApi.model.website_request import WebsiteRequest
globals()['AddressRequest'] = AddressRequest
globals()['EmailRequest'] = EmailRequest
globals()['PhoneRequest'] = PhoneRequest
globals()['WebsiteRequest'] = WebsiteRequest
from eZmaxApi.model.contactinformations_request_compound_all_of import ContactinformationsRequestCompoundAllOf


class TestContactinformationsRequestCompoundAllOf(unittest.TestCase):
    """ContactinformationsRequestCompoundAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testContactinformationsRequestCompoundAllOf(self):
        """Test ContactinformationsRequestCompoundAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ContactinformationsRequestCompoundAllOf()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
