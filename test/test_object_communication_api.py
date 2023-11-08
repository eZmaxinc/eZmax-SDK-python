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

from eZmaxApi.api.object_communication_api import ObjectCommunicationApi  # noqa: E501


class TestObjectCommunicationApi(unittest.TestCase):
    """ObjectCommunicationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectCommunicationApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_communication_send_v1(self) -> None:
        """Test case for communication_send_v1

        Send a new Communication  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
