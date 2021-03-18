"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.37
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.model.apikey_request import ApikeyRequest
from eZmaxinc/eZmax-SDK-python.model.multilingual_apikey_description import MultilingualApikeyDescription
globals()['ApikeyRequest'] = ApikeyRequest
globals()['MultilingualApikeyDescription'] = MultilingualApikeyDescription
from eZmaxinc/eZmax-SDK-python.model.apikey_request_compound import ApikeyRequestCompound


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
