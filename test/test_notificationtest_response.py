"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.8
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.field_pki_notificationsubsection_id import FieldPkiNotificationsubsectionID
from eZmaxApi.model.field_pki_notificationtest_id import FieldPkiNotificationtestID
globals()['FieldPkiNotificationsubsectionID'] = FieldPkiNotificationsubsectionID
globals()['FieldPkiNotificationtestID'] = FieldPkiNotificationtestID
from eZmaxApi.model.notificationtest_response import NotificationtestResponse


class TestNotificationtestResponse(unittest.TestCase):
    """NotificationtestResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotificationtestResponse(self):
        """Test NotificationtestResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotificationtestResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
