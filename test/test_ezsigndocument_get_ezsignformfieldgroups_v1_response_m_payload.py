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

from eZmaxApi.models.ezsigndocument_get_ezsignformfieldgroups_v1_response_m_payload import EzsigndocumentGetEzsignformfieldgroupsV1ResponseMPayload

class TestEzsigndocumentGetEzsignformfieldgroupsV1ResponseMPayload(unittest.TestCase):
    """EzsigndocumentGetEzsignformfieldgroupsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentGetEzsignformfieldgroupsV1ResponseMPayload:
        """Test EzsigndocumentGetEzsignformfieldgroupsV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentGetEzsignformfieldgroupsV1ResponseMPayload`
        """
        model = EzsigndocumentGetEzsignformfieldgroupsV1ResponseMPayload()
        if include_optional:
            return EzsigndocumentGetEzsignformfieldgroupsV1ResponseMPayload(
                a_obj_ezsignformfieldgroup = [
                    eZmaxApi.models.ezsignformfieldgroup_response_compound.ezsignformfieldgroup-ResponseCompound()
                    ]
            )
        else:
            return EzsigndocumentGetEzsignformfieldgroupsV1ResponseMPayload(
                a_obj_ezsignformfieldgroup = [
                    eZmaxApi.models.ezsignformfieldgroup_response_compound.ezsignformfieldgroup-ResponseCompound()
                    ],
        )
        """

    def testEzsigndocumentGetEzsignformfieldgroupsV1ResponseMPayload(self):
        """Test EzsigndocumentGetEzsignformfieldgroupsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
