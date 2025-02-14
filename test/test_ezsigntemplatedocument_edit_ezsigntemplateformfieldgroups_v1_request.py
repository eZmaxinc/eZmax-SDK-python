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

from eZmaxApi.models.ezsigntemplatedocument_edit_ezsigntemplateformfieldgroups_v1_request import EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request

class TestEzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request(unittest.TestCase):
    """EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request:
        """Test EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request`
        """
        model = EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request()
        if include_optional:
            return EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request(
                a_obj_ezsigntemplateformfieldgroup = [
                    eZmaxApi.models.ezsigntemplateformfieldgroup_request_compound.ezsigntemplateformfieldgroup-RequestCompound()
                    ]
            )
        else:
            return EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request(
                a_obj_ezsigntemplateformfieldgroup = [
                    eZmaxApi.models.ezsigntemplateformfieldgroup_request_compound.ezsigntemplateformfieldgroup-RequestCompound()
                    ],
        )
        """

    def testEzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request(self):
        """Test EzsigntemplatedocumentEditEzsigntemplateformfieldgroupsV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
