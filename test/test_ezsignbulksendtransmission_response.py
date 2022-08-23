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
from eZmaxApi.model.common_audit import CommonAudit
from eZmaxApi.model.field_i_ezsignbulksendtransmission_errors import FieldIEzsignbulksendtransmissionErrors
from eZmaxApi.model.field_pki_ezsignbulksend_id import FieldPkiEzsignbulksendID
from eZmaxApi.model.field_pki_ezsignbulksendtransmission_id import FieldPkiEzsignbulksendtransmissionID
globals()['CommonAudit'] = CommonAudit
globals()['FieldIEzsignbulksendtransmissionErrors'] = FieldIEzsignbulksendtransmissionErrors
globals()['FieldPkiEzsignbulksendID'] = FieldPkiEzsignbulksendID
globals()['FieldPkiEzsignbulksendtransmissionID'] = FieldPkiEzsignbulksendtransmissionID
from eZmaxApi.model.ezsignbulksendtransmission_response import EzsignbulksendtransmissionResponse


class TestEzsignbulksendtransmissionResponse(unittest.TestCase):
    """EzsignbulksendtransmissionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsignbulksendtransmissionResponse(self):
        """Test EzsignbulksendtransmissionResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsignbulksendtransmissionResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
