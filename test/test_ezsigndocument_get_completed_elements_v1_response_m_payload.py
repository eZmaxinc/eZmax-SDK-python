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

from eZmaxApi.models.ezsigndocument_get_completed_elements_v1_response_m_payload import EzsigndocumentGetCompletedElementsV1ResponseMPayload

class TestEzsigndocumentGetCompletedElementsV1ResponseMPayload(unittest.TestCase):
    """EzsigndocumentGetCompletedElementsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentGetCompletedElementsV1ResponseMPayload:
        """Test EzsigndocumentGetCompletedElementsV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentGetCompletedElementsV1ResponseMPayload`
        """
        model = EzsigndocumentGetCompletedElementsV1ResponseMPayload()
        if include_optional:
            return EzsigndocumentGetCompletedElementsV1ResponseMPayload(
                a_obj_ezsignsignature = [
                    eZmaxApi.models.ezsignsignature_response_compound.ezsignsignature-ResponseCompound()
                    ],
                a_obj_ezsignformfieldgroup = [
                    eZmaxApi.models.ezsignformfieldgroup_response_compound.ezsignformfieldgroup-ResponseCompound()
                    ]
            )
        else:
            return EzsigndocumentGetCompletedElementsV1ResponseMPayload(
                a_obj_ezsignsignature = [
                    eZmaxApi.models.ezsignsignature_response_compound.ezsignsignature-ResponseCompound()
                    ],
                a_obj_ezsignformfieldgroup = [
                    eZmaxApi.models.ezsignformfieldgroup_response_compound.ezsignformfieldgroup-ResponseCompound()
                    ],
        )
        """

    def testEzsigndocumentGetCompletedElementsV1ResponseMPayload(self):
        """Test EzsigndocumentGetCompletedElementsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
