# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.1
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from eZmaxApi.models.webhook_get_list_v1_response_m_payload import WebhookGetListV1ResponseMPayload

class TestWebhookGetListV1ResponseMPayload(unittest.TestCase):
    """WebhookGetListV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookGetListV1ResponseMPayload:
        """Test WebhookGetListV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookGetListV1ResponseMPayload`
        """
        model = WebhookGetListV1ResponseMPayload()
        if include_optional:
            return WebhookGetListV1ResponseMPayload(
                i_row_returned = 100,
                i_row_filtered = 533,
                a_obj_webhook = [
                    eZmaxApi.models.webhook_list_element.webhook-ListElement(
                        pki_webhook_id = 77, 
                        s_webhook_description = 'Import into our system', 
                        s_webhook_url = 'https://www.example.com', 
                        s_webhook_event = 'Ezsign-DocumentCompleted', 
                        s_webhook_emailfailed = 'email@example.com', 
                        e_webhook_module = 'Ezsign', 
                        e_webhook_ezsignevent = 'FolderCompleted', 
                        e_webhook_managementevent = 'UserCreated', 
                        b_webhook_isactive = True, 
                        b_webhook_issigned = True, )
                    ]
            )
        else:
            return WebhookGetListV1ResponseMPayload(
                i_row_returned = 100,
                i_row_filtered = 533,
                a_obj_webhook = [
                    eZmaxApi.models.webhook_list_element.webhook-ListElement(
                        pki_webhook_id = 77, 
                        s_webhook_description = 'Import into our system', 
                        s_webhook_url = 'https://www.example.com', 
                        s_webhook_event = 'Ezsign-DocumentCompleted', 
                        s_webhook_emailfailed = 'email@example.com', 
                        e_webhook_module = 'Ezsign', 
                        e_webhook_ezsignevent = 'FolderCompleted', 
                        e_webhook_managementevent = 'UserCreated', 
                        b_webhook_isactive = True, 
                        b_webhook_issigned = True, )
                    ],
        )
        """

    def testWebhookGetListV1ResponseMPayload(self):
        """Test WebhookGetListV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
