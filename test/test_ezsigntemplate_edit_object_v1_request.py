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

from eZmaxApi.models.ezsigntemplate_edit_object_v1_request import EzsigntemplateEditObjectV1Request  # noqa: E501

class TestEzsigntemplateEditObjectV1Request(unittest.TestCase):
    """EzsigntemplateEditObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplateEditObjectV1Request:
        """Test EzsigntemplateEditObjectV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplateEditObjectV1Request`
        """
        model = EzsigntemplateEditObjectV1Request()  # noqa: E501
        if include_optional:
            return EzsigntemplateEditObjectV1Request(
                obj_ezsigntemplate = eZmaxApi.models.ezsigntemplate_request_compound.ezsigntemplate-RequestCompound()
            )
        else:
            return EzsigntemplateEditObjectV1Request(
                obj_ezsigntemplate = eZmaxApi.models.ezsigntemplate_request_compound.ezsigntemplate-RequestCompound(),
        )
        """

    def testEzsigntemplateEditObjectV1Request(self):
        """Test EzsigntemplateEditObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
