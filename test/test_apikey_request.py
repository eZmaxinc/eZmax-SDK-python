"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.47
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.multilingual_apikey_description import MultilingualApikeyDescription
globals()['MultilingualApikeyDescription'] = MultilingualApikeyDescription
from eZmaxApi.model.apikey_request import ApikeyRequest


class TestApikeyRequest(unittest.TestCase):
    """ApikeyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApikeyRequest(self):
        """Test ApikeyRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApikeyRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
