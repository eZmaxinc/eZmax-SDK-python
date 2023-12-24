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

from eZmaxApi.models.notificationtest_response import NotificationtestResponse

class TestNotificationtestResponse(unittest.TestCase):
    """NotificationtestResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NotificationtestResponse:
        """Test NotificationtestResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NotificationtestResponse`
        """
        model = NotificationtestResponse()
        if include_optional:
            return NotificationtestResponse(
                pki_notificationtest_id = 14,
                obj_notificationtest_name = eZmaxApi.models.multilingual_notificationtest_name.Multilingual-NotificationtestName(
                    s_notificationtest_name1 = 'Default', 
                    s_notificationtest_name2 = 'Default', ),
                fki_notificationsubsection_id = 3,
                s_notificationtest_function = 'Default',
                s_notificationtest_name_x = 'Default'
            )
        else:
            return NotificationtestResponse(
                pki_notificationtest_id = 14,
                obj_notificationtest_name = eZmaxApi.models.multilingual_notificationtest_name.Multilingual-NotificationtestName(
                    s_notificationtest_name1 = 'Default', 
                    s_notificationtest_name2 = 'Default', ),
                fki_notificationsubsection_id = 3,
                s_notificationtest_function = 'Default',
                s_notificationtest_name_x = 'Default',
        )
        """

    def testNotificationtestResponse(self):
        """Test NotificationtestResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
