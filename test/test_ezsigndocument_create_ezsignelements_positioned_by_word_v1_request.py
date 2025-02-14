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

from eZmaxApi.models.ezsigndocument_create_ezsignelements_positioned_by_word_v1_request import EzsigndocumentCreateEzsignelementsPositionedByWordV1Request

class TestEzsigndocumentCreateEzsignelementsPositionedByWordV1Request(unittest.TestCase):
    """EzsigndocumentCreateEzsignelementsPositionedByWordV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentCreateEzsignelementsPositionedByWordV1Request:
        """Test EzsigndocumentCreateEzsignelementsPositionedByWordV1Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentCreateEzsignelementsPositionedByWordV1Request`
        """
        model = EzsigndocumentCreateEzsignelementsPositionedByWordV1Request()
        if include_optional:
            return EzsigndocumentCreateEzsignelementsPositionedByWordV1Request(
                a_obj_ezsignformfieldgroup = [
                    eZmaxApi.models.custom_ezsignformfieldgroup_create_ezsignelements_positioned_by_word_request.Custom-EzsignformfieldgroupCreateEzsignelementsPositionedByWord-Request()
                    ],
                a_obj_ezsignsignature = [
                    eZmaxApi.models.custom_ezsignsignature_create_ezsignelements_positioned_by_word_request.Custom-EzsignsignatureCreateEzsignelementsPositionedByWord-Request()
                    ]
            )
        else:
            return EzsigndocumentCreateEzsignelementsPositionedByWordV1Request(
                a_obj_ezsignformfieldgroup = [
                    eZmaxApi.models.custom_ezsignformfieldgroup_create_ezsignelements_positioned_by_word_request.Custom-EzsignformfieldgroupCreateEzsignelementsPositionedByWord-Request()
                    ],
                a_obj_ezsignsignature = [
                    eZmaxApi.models.custom_ezsignsignature_create_ezsignelements_positioned_by_word_request.Custom-EzsignsignatureCreateEzsignelementsPositionedByWord-Request()
                    ],
        )
        """

    def testEzsigndocumentCreateEzsignelementsPositionedByWordV1Request(self):
        """Test EzsigndocumentCreateEzsignelementsPositionedByWordV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
