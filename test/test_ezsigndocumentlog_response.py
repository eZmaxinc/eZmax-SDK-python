"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.16
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.field_e_ezsigndocumentlog_type import FieldEEzsigndocumentlogType
from eZmaxApi.model.field_pki_ezsignsigner_id import FieldPkiEzsignsignerID
from eZmaxApi.model.field_pki_user_id import FieldPkiUserID
globals()['FieldEEzsigndocumentlogType'] = FieldEEzsigndocumentlogType
globals()['FieldPkiEzsignsignerID'] = FieldPkiEzsignsignerID
globals()['FieldPkiUserID'] = FieldPkiUserID
from eZmaxApi.model.ezsigndocumentlog_response import EzsigndocumentlogResponse


class TestEzsigndocumentlogResponse(unittest.TestCase):
    """EzsigndocumentlogResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsigndocumentlogResponse(self):
        """Test EzsigndocumentlogResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsigndocumentlogResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
