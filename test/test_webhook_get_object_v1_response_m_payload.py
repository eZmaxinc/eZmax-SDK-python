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
from eZmaxApi.model.field_e_webhook_ezsignevent import FieldEWebhookEzsignevent
from eZmaxApi.model.field_e_webhook_managementevent import FieldEWebhookManagementevent
from eZmaxApi.model.field_e_webhook_module import FieldEWebhookModule
from eZmaxApi.model.field_pki_ezsignfoldertype_id import FieldPkiEzsignfoldertypeID
from eZmaxApi.model.webhook_response_compound import WebhookResponseCompound
globals()['FieldEWebhookEzsignevent'] = FieldEWebhookEzsignevent
globals()['FieldEWebhookManagementevent'] = FieldEWebhookManagementevent
globals()['FieldEWebhookModule'] = FieldEWebhookModule
globals()['FieldPkiEzsignfoldertypeID'] = FieldPkiEzsignfoldertypeID
globals()['WebhookResponseCompound'] = WebhookResponseCompound
from eZmaxApi.model.webhook_get_object_v1_response_m_payload import WebhookGetObjectV1ResponseMPayload


class TestWebhookGetObjectV1ResponseMPayload(unittest.TestCase):
    """WebhookGetObjectV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWebhookGetObjectV1ResponseMPayload(self):
        """Test WebhookGetObjectV1ResponseMPayload"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WebhookGetObjectV1ResponseMPayload()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
