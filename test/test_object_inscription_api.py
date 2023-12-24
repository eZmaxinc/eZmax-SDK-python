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

from eZmaxApi.api.object_inscription_api import ObjectInscriptionApi


class TestObjectInscriptionApi(unittest.TestCase):
    """ObjectInscriptionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectInscriptionApi()

    def tearDown(self) -> None:
        pass

    def test_inscription_get_attachments_v1(self) -> None:
        """Test case for inscription_get_attachments_v1

        Retrieve Inscription's Attachments
        """
        pass

    def test_inscription_get_communication_list_v1(self) -> None:
        """Test case for inscription_get_communication_list_v1

        Retrieve Communication list
        """
        pass

    def test_inscription_get_communicationsenders_v1(self) -> None:
        """Test case for inscription_get_communicationsenders_v1

        Retrieve Inscription's Communicationsender
        """
        pass


if __name__ == '__main__':
    unittest.main()
