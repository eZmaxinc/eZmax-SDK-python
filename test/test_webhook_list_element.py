# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.0
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from eZmaxApi.models.webhook_list_element import WebhookListElement

class TestWebhookListElement(unittest.TestCase):
    """WebhookListElement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookListElement:
        """Test WebhookListElement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookListElement`
        """
        model = WebhookListElement()
        if include_optional:
            return WebhookListElement(
                pki_webhook_id = 77,
                s_webhook_description = 'Import into our system',
                s_webhook_url = 'https://www.example.com',
                s_webhook_event = 'Ezsign-DocumentCompleted',
                s_webhook_emailfailed = 'email@example.com',
                e_webhook_module = 'Ezsign',
                e_webhook_ezsignevent = 'FolderCompleted',
                e_webhook_managementevent = 'UserCreated',
                b_webhook_isactive = True,
                b_webhook_issigned = True
            )
        else:
            return WebhookListElement(
                pki_webhook_id = 77,
                s_webhook_description = 'Import into our system',
                s_webhook_url = 'https://www.example.com',
                s_webhook_event = 'Ezsign-DocumentCompleted',
                s_webhook_emailfailed = 'email@example.com',
                e_webhook_module = 'Ezsign',
                b_webhook_isactive = True,
                b_webhook_issigned = True,
        )
        """

    def testWebhookListElement(self):
        """Test WebhookListElement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
