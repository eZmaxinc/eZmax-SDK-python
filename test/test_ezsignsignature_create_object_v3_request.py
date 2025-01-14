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

from eZmaxApi.models.ezsignsignature_create_object_v3_request import EzsignsignatureCreateObjectV3Request

class TestEzsignsignatureCreateObjectV3Request(unittest.TestCase):
    """EzsignsignatureCreateObjectV3Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignatureCreateObjectV3Request:
        """Test EzsignsignatureCreateObjectV3Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignatureCreateObjectV3Request`
        """
        model = EzsignsignatureCreateObjectV3Request()
        if include_optional:
            return EzsignsignatureCreateObjectV3Request(
                a_obj_ezsignsignature = [
                    eZmaxApi.models.ezsignsignature_request_compound_v2.ezsignsignature-RequestCompoundV2()
                    ]
            )
        else:
            return EzsignsignatureCreateObjectV3Request(
                a_obj_ezsignsignature = [
                    eZmaxApi.models.ezsignsignature_request_compound_v2.ezsignsignature-RequestCompoundV2()
                    ],
        )
        """

    def testEzsignsignatureCreateObjectV3Request(self):
        """Test EzsignsignatureCreateObjectV3Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
