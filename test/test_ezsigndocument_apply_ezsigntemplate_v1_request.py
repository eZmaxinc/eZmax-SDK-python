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

from eZmaxApi.models.ezsigndocument_apply_ezsigntemplate_v1_request import EzsigndocumentApplyEzsigntemplateV1Request

class TestEzsigndocumentApplyEzsigntemplateV1Request(unittest.TestCase):
    """EzsigndocumentApplyEzsigntemplateV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentApplyEzsigntemplateV1Request:
        """Test EzsigndocumentApplyEzsigntemplateV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentApplyEzsigntemplateV1Request`
        """
        model = EzsigndocumentApplyEzsigntemplateV1Request()
        if include_optional:
            return EzsigndocumentApplyEzsigntemplateV1Request(
                fki_ezsigntemplate_id = 36,
                a_s_ezsigntemplatesigner = [
                    'John'
                    ],
                a_pki_ezsignfoldersignerassociation_id = [
                    20
                    ]
            )
        else:
            return EzsigndocumentApplyEzsigntemplateV1Request(
                fki_ezsigntemplate_id = 36,
                a_s_ezsigntemplatesigner = [
                    'John'
                    ],
                a_pki_ezsignfoldersignerassociation_id = [
                    20
                    ],
        )
        """

    def testEzsigndocumentApplyEzsigntemplateV1Request(self):
        """Test EzsigndocumentApplyEzsigntemplateV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
