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

from eZmaxApi.models.ezsignsignature_create_object_v2_request import EzsignsignatureCreateObjectV2Request  # noqa: E501

class TestEzsignsignatureCreateObjectV2Request(unittest.TestCase):
    """EzsignsignatureCreateObjectV2Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignatureCreateObjectV2Request:
        """Test EzsignsignatureCreateObjectV2Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignatureCreateObjectV2Request`
        """
        model = EzsignsignatureCreateObjectV2Request()  # noqa: E501
        if include_optional:
            return EzsignsignatureCreateObjectV2Request(
                a_obj_ezsignsignature = [
                    eZmaxApi.models.ezsignsignature_request_compound.ezsignsignature-RequestCompound()
                    ]
            )
        else:
            return EzsignsignatureCreateObjectV2Request(
                a_obj_ezsignsignature = [
                    eZmaxApi.models.ezsignsignature_request_compound.ezsignsignature-RequestCompound()
                    ],
        )
        """

    def testEzsignsignatureCreateObjectV2Request(self):
        """Test EzsignsignatureCreateObjectV2Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
