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

from eZmaxApi.models.webhook_response_compound import WebhookResponseCompound  # noqa: E501

class TestWebhookResponseCompound(unittest.TestCase):
    """WebhookResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookResponseCompound:
        """Test WebhookResponseCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookResponseCompound`
        """
        model = WebhookResponseCompound()  # noqa: E501
        if include_optional:
            return WebhookResponseCompound(
                pki_webhook_id = 77,
                s_webhook_description = 'Import into our system',
                fki_ezsignfoldertype_id = 5,
                s_ezsignfoldertype_name_x = 'Default',
                e_webhook_module = 'Ezsign',
                e_webhook_ezsignevent = 'FolderCompleted',
                e_webhook_managementevent = 'UserCreated',
                s_webhook_url = 'https://www.example.com',
                s_webhook_emailfailed = 'email@example.com',
                b_webhook_isactive = True,
                b_webhook_skipsslvalidation = False,
                s_webhook_event = 'Ezsign-DocumentCompleted'
            )
        else:
            return WebhookResponseCompound(
                pki_webhook_id = 77,
                s_webhook_description = 'Import into our system',
                e_webhook_module = 'Ezsign',
                s_webhook_url = 'https://www.example.com',
                s_webhook_emailfailed = 'email@example.com',
                b_webhook_skipsslvalidation = False,
                s_webhook_event = 'Ezsign-DocumentCompleted',
        )
        """

    def testWebhookResponseCompound(self):
        """Test WebhookResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
