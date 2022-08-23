"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.10
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.apikey_response import ApikeyResponse
from eZmaxApi.model.common_audit import CommonAudit
from eZmaxApi.model.field_pki_apikey_id import FieldPkiApikeyID
from eZmaxApi.model.multilingual_apikey_description import MultilingualApikeyDescription
globals()['ApikeyResponse'] = ApikeyResponse
globals()['CommonAudit'] = CommonAudit
globals()['FieldPkiApikeyID'] = FieldPkiApikeyID
globals()['MultilingualApikeyDescription'] = MultilingualApikeyDescription
from eZmaxApi.model.apikey_response_compound import ApikeyResponseCompound


class TestApikeyResponseCompound(unittest.TestCase):
    """ApikeyResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApikeyResponseCompound(self):
        """Test ApikeyResponseCompound"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApikeyResponseCompound()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
