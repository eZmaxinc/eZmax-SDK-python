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

from eZmaxApi.models.ezsigndocument_submit_ezsignform_v1_request import EzsigndocumentSubmitEzsignformV1Request

class TestEzsigndocumentSubmitEzsignformV1Request(unittest.TestCase):
    """EzsigndocumentSubmitEzsignformV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentSubmitEzsignformV1Request:
        """Test EzsigndocumentSubmitEzsignformV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentSubmitEzsignformV1Request`
        """
        model = EzsigndocumentSubmitEzsignformV1Request()
        if include_optional:
            return EzsigndocumentSubmitEzsignformV1Request(
                b_ezsignform_isdraft = True,
                a_obj_ezsignformfieldgroup = [
                    eZmaxApi.models.custom_ezsignformfieldgroup_request.Custom-Ezsignformfieldgroup-Request()
                    ]
            )
        else:
            return EzsigndocumentSubmitEzsignformV1Request(
                b_ezsignform_isdraft = True,
                a_obj_ezsignformfieldgroup = [
                    eZmaxApi.models.custom_ezsignformfieldgroup_request.Custom-Ezsignformfieldgroup-Request()
                    ],
        )
        """

    def testEzsigndocumentSubmitEzsignformV1Request(self):
        """Test EzsigndocumentSubmitEzsignformV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
