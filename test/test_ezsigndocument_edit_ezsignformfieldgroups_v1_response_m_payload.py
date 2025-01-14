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

from eZmaxApi.models.ezsigndocument_edit_ezsignformfieldgroups_v1_response_m_payload import EzsigndocumentEditEzsignformfieldgroupsV1ResponseMPayload

class TestEzsigndocumentEditEzsignformfieldgroupsV1ResponseMPayload(unittest.TestCase):
    """EzsigndocumentEditEzsignformfieldgroupsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentEditEzsignformfieldgroupsV1ResponseMPayload:
        """Test EzsigndocumentEditEzsignformfieldgroupsV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentEditEzsignformfieldgroupsV1ResponseMPayload`
        """
        model = EzsigndocumentEditEzsignformfieldgroupsV1ResponseMPayload()
        if include_optional:
            return EzsigndocumentEditEzsignformfieldgroupsV1ResponseMPayload(
                a_pki_ezsignformfieldgroup_id = [
                    26
                    ]
            )
        else:
            return EzsigndocumentEditEzsignformfieldgroupsV1ResponseMPayload(
                a_pki_ezsignformfieldgroup_id = [
                    26
                    ],
        )
        """

    def testEzsigndocumentEditEzsignformfieldgroupsV1ResponseMPayload(self):
        """Test EzsigndocumentEditEzsignformfieldgroupsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
