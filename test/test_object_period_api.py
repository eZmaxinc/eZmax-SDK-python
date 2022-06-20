"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.8
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.object_period_api import ObjectPeriodApi  # noqa: E501


class TestObjectPeriodApi(unittest.TestCase):
    """ObjectPeriodApi unit test stubs"""

    def setUp(self):
        self.api = ObjectPeriodApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_period_get_autocomplete_v1(self):
        """Test case for period_get_autocomplete_v1

        Retrieve Periods and IDs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
