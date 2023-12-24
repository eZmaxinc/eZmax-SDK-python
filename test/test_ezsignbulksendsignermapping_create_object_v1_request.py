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

from eZmaxApi.models.ezsignbulksendsignermapping_create_object_v1_request import EzsignbulksendsignermappingCreateObjectV1Request

class TestEzsignbulksendsignermappingCreateObjectV1Request(unittest.TestCase):
    """EzsignbulksendsignermappingCreateObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignbulksendsignermappingCreateObjectV1Request:
        """Test EzsignbulksendsignermappingCreateObjectV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignbulksendsignermappingCreateObjectV1Request`
        """
        model = EzsignbulksendsignermappingCreateObjectV1Request()
        if include_optional:
            return EzsignbulksendsignermappingCreateObjectV1Request(
                a_obj_ezsignbulksendsignermapping = [
                    eZmaxApi.models.ezsignbulksendsignermapping_request_compound.ezsignbulksendsignermapping-RequestCompound()
                    ]
            )
        else:
            return EzsignbulksendsignermappingCreateObjectV1Request(
                a_obj_ezsignbulksendsignermapping = [
                    eZmaxApi.models.ezsignbulksendsignermapping_request_compound.ezsignbulksendsignermapping-RequestCompound()
                    ],
        )
        """

    def testEzsignbulksendsignermappingCreateObjectV1Request(self):
        """Test EzsignbulksendsignermappingCreateObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
