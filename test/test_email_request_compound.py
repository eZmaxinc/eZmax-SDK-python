"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.9
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.email_request import EmailRequest
from eZmaxApi.model.field_pki_emailtype_id import FieldPkiEmailtypeID
globals()['EmailRequest'] = EmailRequest
globals()['FieldPkiEmailtypeID'] = FieldPkiEmailtypeID
from eZmaxApi.model.email_request_compound import EmailRequestCompound


class TestEmailRequestCompound(unittest.TestCase):
    """EmailRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmailRequestCompound(self):
        """Test EmailRequestCompound"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EmailRequestCompound()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()