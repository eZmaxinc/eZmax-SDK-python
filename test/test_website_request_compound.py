"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.15
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.field_pki_websitetype_id import FieldPkiWebsitetypeID
from eZmaxApi.model.website_request import WebsiteRequest
globals()['FieldPkiWebsitetypeID'] = FieldPkiWebsitetypeID
globals()['WebsiteRequest'] = WebsiteRequest
from eZmaxApi.model.website_request_compound import WebsiteRequestCompound


class TestWebsiteRequestCompound(unittest.TestCase):
    """WebsiteRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWebsiteRequestCompound(self):
        """Test WebsiteRequestCompound"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WebsiteRequestCompound()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
