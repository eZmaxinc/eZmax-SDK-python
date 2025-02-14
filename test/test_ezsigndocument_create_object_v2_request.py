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

from eZmaxApi.models.ezsigndocument_create_object_v2_request import EzsigndocumentCreateObjectV2Request

class TestEzsigndocumentCreateObjectV2Request(unittest.TestCase):
    """EzsigndocumentCreateObjectV2Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentCreateObjectV2Request:
        """Test EzsigndocumentCreateObjectV2Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentCreateObjectV2Request`
        """
        model = EzsigndocumentCreateObjectV2Request()
        if include_optional:
            return EzsigndocumentCreateObjectV2Request(
                a_obj_ezsigndocument = [
                    eZmaxApi.models.ezsigndocument_request_compound.ezsigndocument-RequestCompound()
                    ]
            )
        else:
            return EzsigndocumentCreateObjectV2Request(
                a_obj_ezsigndocument = [
                    eZmaxApi.models.ezsigndocument_request_compound.ezsigndocument-RequestCompound()
                    ],
        )
        """

    def testEzsigndocumentCreateObjectV2Request(self):
        """Test EzsigndocumentCreateObjectV2Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
