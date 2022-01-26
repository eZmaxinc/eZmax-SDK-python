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
from eZmaxApi.model.ezsignsignature_request import EzsignsignatureRequest
from eZmaxApi.model.ezsignsignaturecustomdate_request import EzsignsignaturecustomdateRequest
from eZmaxApi.model.field_e_ezsignsignature_type import FieldEEzsignsignatureType
globals()['EzsignsignatureRequest'] = EzsignsignatureRequest
globals()['EzsignsignaturecustomdateRequest'] = EzsignsignaturecustomdateRequest
globals()['FieldEEzsignsignatureType'] = FieldEEzsignsignatureType
from eZmaxApi.model.ezsignsignature_request_compound import EzsignsignatureRequestCompound


class TestEzsignsignatureRequestCompound(unittest.TestCase):
    """EzsignsignatureRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsignsignatureRequestCompound(self):
        """Test EzsignsignatureRequestCompound"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsignsignatureRequestCompound()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
