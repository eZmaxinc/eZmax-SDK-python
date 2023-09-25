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
import datetime

from eZmaxApi.models.systemconfiguration_edit_object_v1_request import SystemconfigurationEditObjectV1Request  # noqa: E501

class TestSystemconfigurationEditObjectV1Request(unittest.TestCase):
    """SystemconfigurationEditObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemconfigurationEditObjectV1Request:
        """Test SystemconfigurationEditObjectV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SystemconfigurationEditObjectV1Request`
        """
        model = SystemconfigurationEditObjectV1Request()  # noqa: E501
        if include_optional:
            return SystemconfigurationEditObjectV1Request(
                obj_systemconfiguration = eZmaxApi.models.systemconfiguration_request_compound.systemconfiguration-RequestCompound()
            )
        else:
            return SystemconfigurationEditObjectV1Request(
                obj_systemconfiguration = eZmaxApi.models.systemconfiguration_request_compound.systemconfiguration-RequestCompound(),
        )
        """

    def testSystemconfigurationEditObjectV1Request(self):
        """Test SystemconfigurationEditObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
