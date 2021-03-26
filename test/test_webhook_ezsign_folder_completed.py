"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.39
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.attempt_response import AttemptResponse
from eZmaxApi.model.common_webhook import CommonWebhook
from eZmaxApi.model.ezsignfolder_response import EzsignfolderResponse
from eZmaxApi.model.webhook_ezsign_folder_completed_all_of import WebhookEzsignFolderCompletedAllOf
from eZmaxApi.model.webhook_response import WebhookResponse
globals()['AttemptResponse'] = AttemptResponse
globals()['CommonWebhook'] = CommonWebhook
globals()['EzsignfolderResponse'] = EzsignfolderResponse
globals()['WebhookEzsignFolderCompletedAllOf'] = WebhookEzsignFolderCompletedAllOf
globals()['WebhookResponse'] = WebhookResponse
from eZmaxApi.model.webhook_ezsign_folder_completed import WebhookEzsignFolderCompleted


class TestWebhookEzsignFolderCompleted(unittest.TestCase):
    """WebhookEzsignFolderCompleted unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWebhookEzsignFolderCompleted(self):
        """Test WebhookEzsignFolderCompleted"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WebhookEzsignFolderCompleted()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
