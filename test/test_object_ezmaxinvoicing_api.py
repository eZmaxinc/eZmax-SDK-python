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

from eZmaxApi.api.object_ezmaxinvoicing_api import ObjectEzmaxinvoicingApi


class TestObjectEzmaxinvoicingApi(unittest.TestCase):
    """ObjectEzmaxinvoicingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectEzmaxinvoicingApi()

    def tearDown(self) -> None:
        pass

    def test_ezmaxinvoicing_get_autocomplete_v2(self) -> None:
        """Test case for ezmaxinvoicing_get_autocomplete_v2

        Retrieve Ezmaxinvoicings and IDs
        """
        pass

    def test_ezmaxinvoicing_get_object_v2(self) -> None:
        """Test case for ezmaxinvoicing_get_object_v2

        Retrieve an existing Ezmaxinvoicing
        """
        pass

    def test_ezmaxinvoicing_get_provisional_v1(self) -> None:
        """Test case for ezmaxinvoicing_get_provisional_v1

        Retrieve provisional Ezmaxinvoicing
        """
        pass


if __name__ == '__main__':
    unittest.main()
