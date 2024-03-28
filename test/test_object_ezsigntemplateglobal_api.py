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

from eZmaxApi.api.object_ezsigntemplateglobal_api import ObjectEzsigntemplateglobalApi


class TestObjectEzsigntemplateglobalApi(unittest.TestCase):
    """ObjectEzsigntemplateglobalApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectEzsigntemplateglobalApi()

    def tearDown(self) -> None:
        pass

    def test_ezsigntemplateglobal_get_autocomplete_v2(self) -> None:
        """Test case for ezsigntemplateglobal_get_autocomplete_v2

        Retrieve Ezsigntemplateglobals and IDs
        """
        pass

    def test_ezsigntemplateglobal_get_object_v2(self) -> None:
        """Test case for ezsigntemplateglobal_get_object_v2

        Retrieve an existing Ezsigntemplateglobal
        """
        pass


if __name__ == '__main__':
    unittest.main()
