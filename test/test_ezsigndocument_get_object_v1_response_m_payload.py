"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.common_audit import CommonAudit
from eZmaxApi.model.ezsigndocument_response import EzsigndocumentResponse
from eZmaxApi.model.field_e_ezsigndocument_step import FieldEEzsigndocumentStep
from eZmaxApi.model.field_pki_language_id import FieldPkiLanguageID
globals()['CommonAudit'] = CommonAudit
globals()['EzsigndocumentResponse'] = EzsigndocumentResponse
globals()['FieldEEzsigndocumentStep'] = FieldEEzsigndocumentStep
globals()['FieldPkiLanguageID'] = FieldPkiLanguageID
from eZmaxApi.model.ezsigndocument_get_object_v1_response_m_payload import EzsigndocumentGetObjectV1ResponseMPayload


class TestEzsigndocumentGetObjectV1ResponseMPayload(unittest.TestCase):
    """EzsigndocumentGetObjectV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsigndocumentGetObjectV1ResponseMPayload(self):
        """Test EzsigndocumentGetObjectV1ResponseMPayload"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsigndocumentGetObjectV1ResponseMPayload()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
