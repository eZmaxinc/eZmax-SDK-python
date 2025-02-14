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

from eZmaxApi.models.ezsignsignature_edit_object_v2_request import EzsignsignatureEditObjectV2Request

class TestEzsignsignatureEditObjectV2Request(unittest.TestCase):
    """EzsignsignatureEditObjectV2Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignatureEditObjectV2Request:
        """Test EzsignsignatureEditObjectV2Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignatureEditObjectV2Request`
        """
        model = EzsignsignatureEditObjectV2Request()
        if include_optional:
            return EzsignsignatureEditObjectV2Request(
                obj_ezsignsignature = eZmaxApi.models.ezsignsignature_request_compound_v2.ezsignsignature-RequestCompoundV2()
            )
        else:
            return EzsignsignatureEditObjectV2Request(
                obj_ezsignsignature = eZmaxApi.models.ezsignsignature_request_compound_v2.ezsignsignature-RequestCompoundV2(),
        )
        """

    def testEzsignsignatureEditObjectV2Request(self):
        """Test EzsignsignatureEditObjectV2Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
