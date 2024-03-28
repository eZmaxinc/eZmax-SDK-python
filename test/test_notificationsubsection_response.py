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

from eZmaxApi.models.notificationsubsection_response import NotificationsubsectionResponse

class TestNotificationsubsectionResponse(unittest.TestCase):
    """NotificationsubsectionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NotificationsubsectionResponse:
        """Test NotificationsubsectionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NotificationsubsectionResponse`
        """
        model = NotificationsubsectionResponse()
        if include_optional:
            return NotificationsubsectionResponse(
                pki_notificationsubsection_id = 3,
                fki_notificationsection_id = 1,
                obj_notificationsubsection_name = eZmaxApi.models.multilingual_notificationsubsection_name.Multilingual-NotificationsubsectionName(
                    s_notificationsubsection_name1 = 'Signature électronique', 
                    s_notificationsubsection_name2 = 'Electronic signature', ),
                s_notificationsection_name_x = 'Homepage',
                s_notificationsubsection_name_x = 'Default'
            )
        else:
            return NotificationsubsectionResponse(
                pki_notificationsubsection_id = 3,
                fki_notificationsection_id = 1,
                s_notificationsubsection_name_x = 'Default',
        )
        """

    def testNotificationsubsectionResponse(self):
        """Test NotificationsubsectionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
