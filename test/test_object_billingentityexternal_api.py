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

from eZmaxApi.api.object_billingentityexternal_api import ObjectBillingentityexternalApi


class TestObjectBillingentityexternalApi(unittest.TestCase):
    """ObjectBillingentityexternalApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectBillingentityexternalApi()

    def tearDown(self) -> None:
        pass

    def test_billingentityexternal_get_autocomplete_v2(self) -> None:
        """Test case for billingentityexternal_get_autocomplete_v2

        Retrieve Billingentityexternals and IDs
        """
        pass


if __name__ == '__main__':
    unittest.main()
