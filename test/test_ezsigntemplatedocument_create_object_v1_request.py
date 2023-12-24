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

from eZmaxApi.models.ezsigntemplatedocument_create_object_v1_request import EzsigntemplatedocumentCreateObjectV1Request

class TestEzsigntemplatedocumentCreateObjectV1Request(unittest.TestCase):
    """EzsigntemplatedocumentCreateObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatedocumentCreateObjectV1Request:
        """Test EzsigntemplatedocumentCreateObjectV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatedocumentCreateObjectV1Request`
        """
        model = EzsigntemplatedocumentCreateObjectV1Request()
        if include_optional:
            return EzsigntemplatedocumentCreateObjectV1Request(
                a_obj_ezsigntemplatedocument = [
                    eZmaxApi.models.ezsigntemplatedocument_request_compound.ezsigntemplatedocument-RequestCompound()
                    ]
            )
        else:
            return EzsigntemplatedocumentCreateObjectV1Request(
                a_obj_ezsigntemplatedocument = [
                    eZmaxApi.models.ezsigntemplatedocument_request_compound.ezsigntemplatedocument-RequestCompound()
                    ],
        )
        """

    def testEzsigntemplatedocumentCreateObjectV1Request(self):
        """Test EzsigntemplatedocumentCreateObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
