"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.13
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.object_notificationsection_api import ObjectNotificationsectionApi  # noqa: E501


class TestObjectNotificationsectionApi(unittest.TestCase):
    """ObjectNotificationsectionApi unit test stubs"""

    def setUp(self):
        self.api = ObjectNotificationsectionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_notificationsection_get_notificationtests_v1(self):
        """Test case for notificationsection_get_notificationtests_v1

        Retrieve an existing Notificationsection's Notificationtests  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
