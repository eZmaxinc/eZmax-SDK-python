"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.38
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.apikey_request import ApikeyRequest
from eZmaxApi.model.apikey_request_compound import ApikeyRequestCompound
globals()['ApikeyRequest'] = ApikeyRequest
globals()['ApikeyRequestCompound'] = ApikeyRequestCompound
from eZmaxApi.model.apikey_create_object_v1_request import ApikeyCreateObjectV1Request


class TestApikeyCreateObjectV1Request(unittest.TestCase):
    """ApikeyCreateObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApikeyCreateObjectV1Request(self):
        """Test ApikeyCreateObjectV1Request"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApikeyCreateObjectV1Request()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
