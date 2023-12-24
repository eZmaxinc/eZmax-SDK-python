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

from eZmaxApi.api.object_notificationsection_api import ObjectNotificationsectionApi


class TestObjectNotificationsectionApi(unittest.TestCase):
    """ObjectNotificationsectionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectNotificationsectionApi()

    def tearDown(self) -> None:
        pass

    def test_notificationsection_get_notificationtests_v1(self) -> None:
        """Test case for notificationsection_get_notificationtests_v1

        Retrieve an existing Notificationsection's Notificationtests
        """
        pass


if __name__ == '__main__':
    unittest.main()
