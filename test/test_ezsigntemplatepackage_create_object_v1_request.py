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

from eZmaxApi.models.ezsigntemplatepackage_create_object_v1_request import EzsigntemplatepackageCreateObjectV1Request

class TestEzsigntemplatepackageCreateObjectV1Request(unittest.TestCase):
    """EzsigntemplatepackageCreateObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatepackageCreateObjectV1Request:
        """Test EzsigntemplatepackageCreateObjectV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatepackageCreateObjectV1Request`
        """
        model = EzsigntemplatepackageCreateObjectV1Request()
        if include_optional:
            return EzsigntemplatepackageCreateObjectV1Request(
                a_obj_ezsigntemplatepackage = [
                    eZmaxApi.models.ezsigntemplatepackage_request_compound.ezsigntemplatepackage-RequestCompound()
                    ]
            )
        else:
            return EzsigntemplatepackageCreateObjectV1Request(
                a_obj_ezsigntemplatepackage = [
                    eZmaxApi.models.ezsigntemplatepackage_request_compound.ezsigntemplatepackage-RequestCompound()
                    ],
        )
        """

    def testEzsigntemplatepackageCreateObjectV1Request(self):
        """Test EzsigntemplatepackageCreateObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
