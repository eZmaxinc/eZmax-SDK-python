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

from eZmaxApi.api.module_ezsign_api import ModuleEzsignApi  # noqa: E501


class TestModuleEzsignApi(unittest.TestCase):
    """ModuleEzsignApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ModuleEzsignApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_ezsign_suggest_signers_v1(self) -> None:
        """Test case for ezsign_suggest_signers_v1

        Suggest signers  # noqa: E501
        """
        pass

    def test_ezsign_suggest_templates_v1(self) -> None:
        """Test case for ezsign_suggest_templates_v1

        Suggest templates  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
