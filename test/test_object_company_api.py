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

from eZmaxApi.api.object_company_api import ObjectCompanyApi


class TestObjectCompanyApi(unittest.TestCase):
    """ObjectCompanyApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectCompanyApi()

    def tearDown(self) -> None:
        pass

    def test_company_get_autocomplete_v2(self) -> None:
        """Test case for company_get_autocomplete_v2

        Retrieve Companys and IDs
        """
        pass


if __name__ == '__main__':
    unittest.main()
