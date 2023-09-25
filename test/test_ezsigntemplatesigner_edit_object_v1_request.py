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

from eZmaxApi.models.ezsigntemplatesigner_edit_object_v1_request import EzsigntemplatesignerEditObjectV1Request  # noqa: E501

class TestEzsigntemplatesignerEditObjectV1Request(unittest.TestCase):
    """EzsigntemplatesignerEditObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatesignerEditObjectV1Request:
        """Test EzsigntemplatesignerEditObjectV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatesignerEditObjectV1Request`
        """
        model = EzsigntemplatesignerEditObjectV1Request()  # noqa: E501
        if include_optional:
            return EzsigntemplatesignerEditObjectV1Request(
                obj_ezsigntemplatesigner = eZmaxApi.models.ezsigntemplatesigner_request_compound.ezsigntemplatesigner-RequestCompound()
            )
        else:
            return EzsigntemplatesignerEditObjectV1Request(
                obj_ezsigntemplatesigner = eZmaxApi.models.ezsigntemplatesigner_request_compound.ezsigntemplatesigner-RequestCompound(),
        )
        """

    def testEzsigntemplatesignerEditObjectV1Request(self):
        """Test EzsigntemplatesignerEditObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
