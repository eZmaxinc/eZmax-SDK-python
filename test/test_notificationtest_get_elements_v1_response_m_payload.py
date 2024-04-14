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

from eZmaxApi.models.notificationtest_get_elements_v1_response_m_payload import NotificationtestGetElementsV1ResponseMPayload

class TestNotificationtestGetElementsV1ResponseMPayload(unittest.TestCase):
    """NotificationtestGetElementsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NotificationtestGetElementsV1ResponseMPayload:
        """Test NotificationtestGetElementsV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NotificationtestGetElementsV1ResponseMPayload`
        """
        model = NotificationtestGetElementsV1ResponseMPayload()
        if include_optional:
            return NotificationtestGetElementsV1ResponseMPayload(
                pki_notificationtest_id = 14,
                s_notificationtest_function = 'Default',
                a_s_variableobject_property = [
                    'PropertyName1'
                    ],
                a_obj_variableobject = [
                    { }
                    ]
            )
        else:
            return NotificationtestGetElementsV1ResponseMPayload(
                pki_notificationtest_id = 14,
                s_notificationtest_function = 'Default',
                a_s_variableobject_property = [
                    'PropertyName1'
                    ],
                a_obj_variableobject = [
                    { }
                    ],
        )
        """

    def testNotificationtestGetElementsV1ResponseMPayload(self):
        """Test NotificationtestGetElementsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
