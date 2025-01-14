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

from eZmaxApi.api.object_otherincome_api import ObjectOtherincomeApi


class TestObjectOtherincomeApi(unittest.TestCase):
    """ObjectOtherincomeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectOtherincomeApi()

    def tearDown(self) -> None:
        pass

    def test_otherincome_get_communication_count_v1(self) -> None:
        """Test case for otherincome_get_communication_count_v1

        Retrieve Communication count
        """
        pass

    def test_otherincome_get_communication_list_v1(self) -> None:
        """Test case for otherincome_get_communication_list_v1

        Retrieve Communication list
        """
        pass

    def test_otherincome_get_communicationrecipients_v1(self) -> None:
        """Test case for otherincome_get_communicationrecipients_v1

        Retrieve Otherincome's Communicationrecipient
        """
        pass

    def test_otherincome_get_communicationsenders_v1(self) -> None:
        """Test case for otherincome_get_communicationsenders_v1

        Retrieve Otherincome's Communicationsender
        """
        pass


if __name__ == '__main__':
    unittest.main()
