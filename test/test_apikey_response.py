"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.31
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.model.common_audit import CommonAudit
from eZmaxinc/eZmax-SDK-python.model.multilingual_apikey_description import MultilingualApikeyDescription
globals()['CommonAudit'] = CommonAudit
globals()['MultilingualApikeyDescription'] = MultilingualApikeyDescription
from eZmaxinc/eZmax-SDK-python.model.apikey_response import ApikeyResponse


class TestApikeyResponse(unittest.TestCase):
    """ApikeyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApikeyResponse(self):
        """Test ApikeyResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApikeyResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
