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

from eZmaxApi.models.ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1_response_m_payload import EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1ResponseMPayload  # noqa: E501

class TestEzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1ResponseMPayload(unittest.TestCase):
    """EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1ResponseMPayload:
        """Test EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1ResponseMPayload`
        """
        model = EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1ResponseMPayload()  # noqa: E501
        if include_optional:
            return EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1ResponseMPayload(
                a_obj_ezsigntemplateformfieldgroup = [
                    eZmaxApi.models.ezsigntemplateformfieldgroup_response_compound.ezsigntemplateformfieldgroup-ResponseCompound()
                    ]
            )
        else:
            return EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1ResponseMPayload(
                a_obj_ezsigntemplateformfieldgroup = [
                    eZmaxApi.models.ezsigntemplateformfieldgroup_response_compound.ezsigntemplateformfieldgroup-ResponseCompound()
                    ],
        )
        """

    def testEzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1ResponseMPayload(self):
        """Test EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
