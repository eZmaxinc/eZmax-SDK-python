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

from eZmaxApi.models.webhook_userstaged_userstaged_created import WebhookUserstagedUserstagedCreated  # noqa: E501

class TestWebhookUserstagedUserstagedCreated(unittest.TestCase):
    """WebhookUserstagedUserstagedCreated unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookUserstagedUserstagedCreated:
        """Test WebhookUserstagedUserstagedCreated
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookUserstagedUserstagedCreated`
        """
        model = WebhookUserstagedUserstagedCreated()  # noqa: E501
        if include_optional:
            return WebhookUserstagedUserstagedCreated(
                obj_webhook = eZmaxApi.models.custom_webhook_response.Custom-Webhook-Response(),
                a_obj_attempt = [
                    eZmaxApi.models.attempt_response_compound.attempt-ResponseCompound()
                    ],
                obj_userstaged = eZmaxApi.models.userstaged_response_compound.userstaged-ResponseCompound()
            )
        else:
            return WebhookUserstagedUserstagedCreated(
                obj_webhook = eZmaxApi.models.custom_webhook_response.Custom-Webhook-Response(),
                a_obj_attempt = [
                    eZmaxApi.models.attempt_response_compound.attempt-ResponseCompound()
                    ],
                obj_userstaged = eZmaxApi.models.userstaged_response_compound.userstaged-ResponseCompound(),
        )
        """

    def testWebhookUserstagedUserstagedCreated(self):
        """Test WebhookUserstagedUserstagedCreated"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
