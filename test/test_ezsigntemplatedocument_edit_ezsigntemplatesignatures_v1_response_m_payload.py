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

from eZmaxApi.models.ezsigntemplatedocument_edit_ezsigntemplatesignatures_v1_response_m_payload import EzsigntemplatedocumentEditEzsigntemplatesignaturesV1ResponseMPayload

class TestEzsigntemplatedocumentEditEzsigntemplatesignaturesV1ResponseMPayload(unittest.TestCase):
    """EzsigntemplatedocumentEditEzsigntemplatesignaturesV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatedocumentEditEzsigntemplatesignaturesV1ResponseMPayload:
        """Test EzsigntemplatedocumentEditEzsigntemplatesignaturesV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatedocumentEditEzsigntemplatesignaturesV1ResponseMPayload`
        """
        model = EzsigntemplatedocumentEditEzsigntemplatesignaturesV1ResponseMPayload()
        if include_optional:
            return EzsigntemplatedocumentEditEzsigntemplatesignaturesV1ResponseMPayload(
                a_pki_ezsigntemplatesignature_id = [
                    99
                    ]
            )
        else:
            return EzsigntemplatedocumentEditEzsigntemplatesignaturesV1ResponseMPayload(
                a_pki_ezsigntemplatesignature_id = [
                    99
                    ],
        )
        """

    def testEzsigntemplatedocumentEditEzsigntemplatesignaturesV1ResponseMPayload(self):
        """Test EzsigntemplatedocumentEditEzsigntemplatesignaturesV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
