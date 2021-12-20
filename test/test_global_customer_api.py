"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.4
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.global_customer_api import GlobalCustomerApi  # noqa: E501


class TestGlobalCustomerApi(unittest.TestCase):
    """GlobalCustomerApi unit test stubs"""

    def setUp(self):
        self.api = GlobalCustomerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_global_customer_get_endpoint_v1(self):
        """Test case for global_customer_get_endpoint_v1

        Get customer endpoint  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
