"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.12
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.field_pki_notificationsection_id import FieldPkiNotificationsectionID
from eZmaxApi.model.field_pki_notificationsubsection_id import FieldPkiNotificationsubsectionID
from eZmaxApi.model.multilingual_notificationsubsection_name import MultilingualNotificationsubsectionName
globals()['FieldPkiNotificationsectionID'] = FieldPkiNotificationsectionID
globals()['FieldPkiNotificationsubsectionID'] = FieldPkiNotificationsubsectionID
globals()['MultilingualNotificationsubsectionName'] = MultilingualNotificationsubsectionName
from eZmaxApi.model.notificationsubsection_response import NotificationsubsectionResponse


class TestNotificationsubsectionResponse(unittest.TestCase):
    """NotificationsubsectionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotificationsubsectionResponse(self):
        """Test NotificationsubsectionResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotificationsubsectionResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
