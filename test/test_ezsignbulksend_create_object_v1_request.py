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

from eZmaxApi.models.ezsignbulksend_create_object_v1_request import EzsignbulksendCreateObjectV1Request

class TestEzsignbulksendCreateObjectV1Request(unittest.TestCase):
    """EzsignbulksendCreateObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignbulksendCreateObjectV1Request:
        """Test EzsignbulksendCreateObjectV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignbulksendCreateObjectV1Request`
        """
        model = EzsignbulksendCreateObjectV1Request()
        if include_optional:
            return EzsignbulksendCreateObjectV1Request(
                a_obj_ezsignbulksend = [
                    eZmaxApi.models.ezsignbulksend_request_compound.ezsignbulksend-RequestCompound()
                    ]
            )
        else:
            return EzsignbulksendCreateObjectV1Request(
                a_obj_ezsignbulksend = [
                    eZmaxApi.models.ezsignbulksend_request_compound.ezsignbulksend-RequestCompound()
                    ],
        )
        """

    def testEzsignbulksendCreateObjectV1Request(self):
        """Test EzsignbulksendCreateObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
