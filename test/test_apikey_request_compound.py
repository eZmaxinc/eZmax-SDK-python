"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.5
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.apikey_request import ApikeyRequest
from eZmaxApi.model.multilingual_apikey_description import MultilingualApikeyDescription
globals()['ApikeyRequest'] = ApikeyRequest
globals()['MultilingualApikeyDescription'] = MultilingualApikeyDescription
from eZmaxApi.model.apikey_request_compound import ApikeyRequestCompound


class TestApikeyRequestCompound(unittest.TestCase):
    """ApikeyRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApikeyRequestCompound(self):
        """Test ApikeyRequestCompound"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApikeyRequestCompound()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
