"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.13
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.object_notificationtest_api import ObjectNotificationtestApi  # noqa: E501


class TestObjectNotificationtestApi(unittest.TestCase):
    """ObjectNotificationtestApi unit test stubs"""

    def setUp(self):
        self.api = ObjectNotificationtestApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_notificationtest_get_elements_v1(self):
        """Test case for notificationtest_get_elements_v1

        Retrieve an existing Notificationtest's Elements  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
