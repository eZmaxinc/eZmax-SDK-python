"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.13
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.field_pki_ezsignbulksend_id import FieldPkiEzsignbulksendID
from eZmaxApi.model.field_pki_ezsignbulksendsignermapping_id import FieldPkiEzsignbulksendsignermappingID
from eZmaxApi.model.field_pki_user_id import FieldPkiUserID
globals()['FieldPkiEzsignbulksendID'] = FieldPkiEzsignbulksendID
globals()['FieldPkiEzsignbulksendsignermappingID'] = FieldPkiEzsignbulksendsignermappingID
globals()['FieldPkiUserID'] = FieldPkiUserID
from eZmaxApi.model.ezsignbulksendsignermapping_request import EzsignbulksendsignermappingRequest


class TestEzsignbulksendsignermappingRequest(unittest.TestCase):
    """EzsignbulksendsignermappingRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsignbulksendsignermappingRequest(self):
        """Test EzsignbulksendsignermappingRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsignbulksendsignermappingRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
