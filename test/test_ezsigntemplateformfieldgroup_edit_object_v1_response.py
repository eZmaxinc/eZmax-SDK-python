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

from eZmaxApi.models.ezsigntemplateformfieldgroup_edit_object_v1_response import EzsigntemplateformfieldgroupEditObjectV1Response

class TestEzsigntemplateformfieldgroupEditObjectV1Response(unittest.TestCase):
    """EzsigntemplateformfieldgroupEditObjectV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplateformfieldgroupEditObjectV1Response:
        """Test EzsigntemplateformfieldgroupEditObjectV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplateformfieldgroupEditObjectV1Response`
        """
        model = EzsigntemplateformfieldgroupEditObjectV1Response()
        if include_optional:
            return EzsigntemplateformfieldgroupEditObjectV1Response(
            )
        else:
            return EzsigntemplateformfieldgroupEditObjectV1Response(
        )
        """

    def testEzsigntemplateformfieldgroupEditObjectV1Response(self):
        """Test EzsigntemplateformfieldgroupEditObjectV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
