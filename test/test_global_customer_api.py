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

from eZmaxApi.api.global_customer_api import GlobalCustomerApi


class TestGlobalCustomerApi(unittest.TestCase):
    """GlobalCustomerApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GlobalCustomerApi()

    def tearDown(self) -> None:
        pass

    def test_global_customer_get_endpoint_v1(self) -> None:
        """Test case for global_customer_get_endpoint_v1

        Get customer endpoint
        """
        pass


if __name__ == '__main__':
    unittest.main()
