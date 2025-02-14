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

from eZmaxApi.models.ezsignbulksenddocumentmapping_create_object_v1_request import EzsignbulksenddocumentmappingCreateObjectV1Request

class TestEzsignbulksenddocumentmappingCreateObjectV1Request(unittest.TestCase):
    """EzsignbulksenddocumentmappingCreateObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignbulksenddocumentmappingCreateObjectV1Request:
        """Test EzsignbulksenddocumentmappingCreateObjectV1Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignbulksenddocumentmappingCreateObjectV1Request`
        """
        model = EzsignbulksenddocumentmappingCreateObjectV1Request()
        if include_optional:
            return EzsignbulksenddocumentmappingCreateObjectV1Request(
                a_obj_ezsignbulksenddocumentmapping = [
                    eZmaxApi.models.ezsignbulksenddocumentmapping_request_compound.ezsignbulksenddocumentmapping-RequestCompound()
                    ]
            )
        else:
            return EzsignbulksenddocumentmappingCreateObjectV1Request(
                a_obj_ezsignbulksenddocumentmapping = [
                    eZmaxApi.models.ezsignbulksenddocumentmapping_request_compound.ezsignbulksenddocumentmapping-RequestCompound()
                    ],
        )
        """

    def testEzsignbulksenddocumentmappingCreateObjectV1Request(self):
        """Test EzsignbulksenddocumentmappingCreateObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
