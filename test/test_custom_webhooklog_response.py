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

from eZmaxApi.models.custom_webhooklog_response import CustomWebhooklogResponse  # noqa: E501

class TestCustomWebhooklogResponse(unittest.TestCase):
    """CustomWebhooklogResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomWebhooklogResponse:
        """Test CustomWebhooklogResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomWebhooklogResponse`
        """
        model = CustomWebhooklogResponse()  # noqa: E501
        if include_optional:
            return CustomWebhooklogResponse(
                dt_webhooklog_date = '2020-12-31 23:59:59',
                t_webhooklog_json = '{}'
            )
        else:
            return CustomWebhooklogResponse(
                dt_webhooklog_date = '2020-12-31 23:59:59',
                t_webhooklog_json = '{}',
        )
        """

    def testCustomWebhooklogResponse(self):
        """Test CustomWebhooklogResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
