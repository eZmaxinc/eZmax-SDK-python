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

from eZmaxApi.api.object_notificationtest_api import ObjectNotificationtestApi


class TestObjectNotificationtestApi(unittest.TestCase):
    """ObjectNotificationtestApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectNotificationtestApi()

    def tearDown(self) -> None:
        pass

    def test_notificationtest_get_elements_v1(self) -> None:
        """Test case for notificationtest_get_elements_v1

        Retrieve an existing Notificationtest's Elements
        """
        pass


if __name__ == '__main__':
    unittest.main()
