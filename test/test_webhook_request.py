"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.14
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
globals()['FieldEWebhookEzsignevent'] = FieldEWebhookEzsignevent
globals()['FieldEWebhookManagementevent'] = FieldEWebhookManagementevent
globals()['FieldEWebhookModule'] = FieldEWebhookModule
globals()['FieldPkiEzsignfoldertypeID'] = FieldPkiEzsignfoldertypeID
from eZmaxApi.model.webhook_request import WebhookRequest


class TestWebhookRequest(unittest.TestCase):
    """WebhookRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWebhookRequest(self):
        """Test WebhookRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WebhookRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
