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

from eZmaxApi.api.object_webhook_api import ObjectWebhookApi


class TestObjectWebhookApi(unittest.TestCase):
    """ObjectWebhookApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectWebhookApi()

    def tearDown(self) -> None:
        pass

    def test_webhook_create_object_v2(self) -> None:
        """Test case for webhook_create_object_v2

        Create a new Webhook
        """
        pass

    def test_webhook_delete_object_v1(self) -> None:
        """Test case for webhook_delete_object_v1

        Delete an existing Webhook
        """
        pass

    def test_webhook_edit_object_v1(self) -> None:
        """Test case for webhook_edit_object_v1

        Edit an existing Webhook
        """
        pass

    def test_webhook_get_history_v1(self) -> None:
        """Test case for webhook_get_history_v1

        Retrieve the logs for recent Webhook calls
        """
        pass

    def test_webhook_get_list_v1(self) -> None:
        """Test case for webhook_get_list_v1

        Retrieve Webhook list
        """
        pass

    def test_webhook_get_object_v2(self) -> None:
        """Test case for webhook_get_object_v2

        Retrieve an existing Webhook
        """
        pass

    def test_webhook_regenerate_apikey_v1(self) -> None:
        """Test case for webhook_regenerate_apikey_v1

        Regenerate the Apikey
        """
        pass

    def test_webhook_send_webhook_v1(self) -> None:
        """Test case for webhook_send_webhook_v1

        Emit a Webhook event
        """
        pass

    def test_webhook_test_v1(self) -> None:
        """Test case for webhook_test_v1

        Test the Webhook by calling the Url
        """
        pass


if __name__ == '__main__':
    unittest.main()
