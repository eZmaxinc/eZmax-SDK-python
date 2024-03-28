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

from eZmaxApi.models.ezsigndocument_apply_ezsigntemplateglobal_v1_request import EzsigndocumentApplyEzsigntemplateglobalV1Request

class TestEzsigndocumentApplyEzsigntemplateglobalV1Request(unittest.TestCase):
    """EzsigndocumentApplyEzsigntemplateglobalV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentApplyEzsigntemplateglobalV1Request:
        """Test EzsigndocumentApplyEzsigntemplateglobalV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentApplyEzsigntemplateglobalV1Request`
        """
        model = EzsigndocumentApplyEzsigntemplateglobalV1Request()
        if include_optional:
            return EzsigndocumentApplyEzsigntemplateglobalV1Request(
                fki_ezsigntemplateglobal_id = 36,
                a_s_ezsigntemplateglobalsigner = [
                    'John'
                    ],
                a_pki_ezsignfoldersignerassociation_id = [
                    20
                    ]
            )
        else:
            return EzsigndocumentApplyEzsigntemplateglobalV1Request(
                fki_ezsigntemplateglobal_id = 36,
                a_s_ezsigntemplateglobalsigner = [
                    'John'
                    ],
                a_pki_ezsignfoldersignerassociation_id = [
                    20
                    ],
        )
        """

    def testEzsigndocumentApplyEzsigntemplateglobalV1Request(self):
        """Test EzsigndocumentApplyEzsigntemplateglobalV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
