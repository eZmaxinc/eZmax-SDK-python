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

from eZmaxApi.api.object_communication_api import ObjectCommunicationApi


class TestObjectCommunicationApi(unittest.TestCase):
    """ObjectCommunicationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectCommunicationApi()

    def tearDown(self) -> None:
        pass

    def test_communication_get_communication_body_v1(self) -> None:
        """Test case for communication_get_communication_body_v1

        Retrieve the communication body.
        """
        pass

    def test_communication_send_v1(self) -> None:
        """Test case for communication_send_v1

        Send a new Communication
        """
        pass


if __name__ == '__main__':
    unittest.main()
