"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.37
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.model.attempt_response import AttemptResponse
from eZmaxinc/eZmax-SDK-python.model.common_webhook import CommonWebhook
from eZmaxinc/eZmax-SDK-python.model.ezsigndocument_response import EzsigndocumentResponse
from eZmaxinc/eZmax-SDK-python.model.webhook_ezsign_document_completed_all_of import WebhookEzsignDocumentCompletedAllOf
from eZmaxinc/eZmax-SDK-python.model.webhook_response import WebhookResponse
globals()['AttemptResponse'] = AttemptResponse
globals()['CommonWebhook'] = CommonWebhook
globals()['EzsigndocumentResponse'] = EzsigndocumentResponse
globals()['WebhookEzsignDocumentCompletedAllOf'] = WebhookEzsignDocumentCompletedAllOf
globals()['WebhookResponse'] = WebhookResponse
from eZmaxinc/eZmax-SDK-python.model.webhook_ezsign_document_completed import WebhookEzsignDocumentCompleted


class TestWebhookEzsignDocumentCompleted(unittest.TestCase):
    """WebhookEzsignDocumentCompleted unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWebhookEzsignDocumentCompleted(self):
        """Test WebhookEzsignDocumentCompleted"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WebhookEzsignDocumentCompleted()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
