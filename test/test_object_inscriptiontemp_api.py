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

from eZmaxApi.api.object_inscriptiontemp_api import ObjectInscriptiontempApi


class TestObjectInscriptiontempApi(unittest.TestCase):
    """ObjectInscriptiontempApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectInscriptiontempApi()

    def tearDown(self) -> None:
        pass

    def test_inscriptiontemp_get_communication_list_v1(self) -> None:
        """Test case for inscriptiontemp_get_communication_list_v1

        Retrieve Communication list
        """
        pass


if __name__ == '__main__':
    unittest.main()
