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

from eZmaxApi.models.ezsignsigningreason_create_object_v1_request import EzsignsigningreasonCreateObjectV1Request

class TestEzsignsigningreasonCreateObjectV1Request(unittest.TestCase):
    """EzsignsigningreasonCreateObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsigningreasonCreateObjectV1Request:
        """Test EzsignsigningreasonCreateObjectV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsigningreasonCreateObjectV1Request`
        """
        model = EzsignsigningreasonCreateObjectV1Request()
        if include_optional:
            return EzsignsigningreasonCreateObjectV1Request(
                a_obj_ezsignsigningreason = [
                    eZmaxApi.models.ezsignsigningreason_request_compound.ezsignsigningreason-RequestCompound()
                    ]
            )
        else:
            return EzsignsigningreasonCreateObjectV1Request(
                a_obj_ezsignsigningreason = [
                    eZmaxApi.models.ezsignsigningreason_request_compound.ezsignsigningreason-RequestCompound()
                    ],
        )
        """

    def testEzsignsigningreasonCreateObjectV1Request(self):
        """Test EzsignsigningreasonCreateObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
