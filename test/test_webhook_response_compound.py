"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.12
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
from eZmaxApi.model.webhook_response import WebhookResponse
globals()['FieldEWebhookEzsignevent'] = FieldEWebhookEzsignevent
globals()['FieldEWebhookManagementevent'] = FieldEWebhookManagementevent
globals()['FieldEWebhookModule'] = FieldEWebhookModule
globals()['FieldPkiEzsignfoldertypeID'] = FieldPkiEzsignfoldertypeID
globals()['WebhookResponse'] = WebhookResponse
from eZmaxApi.model.webhook_response_compound import WebhookResponseCompound


class TestWebhookResponseCompound(unittest.TestCase):
    """WebhookResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWebhookResponseCompound(self):
        """Test WebhookResponseCompound"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WebhookResponseCompound()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
