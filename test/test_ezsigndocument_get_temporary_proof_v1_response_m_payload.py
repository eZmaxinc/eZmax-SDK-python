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

from eZmaxApi.models.ezsigndocument_get_temporary_proof_v1_response_m_payload import EzsigndocumentGetTemporaryProofV1ResponseMPayload

class TestEzsigndocumentGetTemporaryProofV1ResponseMPayload(unittest.TestCase):
    """EzsigndocumentGetTemporaryProofV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentGetTemporaryProofV1ResponseMPayload:
        """Test EzsigndocumentGetTemporaryProofV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentGetTemporaryProofV1ResponseMPayload`
        """
        model = EzsigndocumentGetTemporaryProofV1ResponseMPayload()
        if include_optional:
            return EzsigndocumentGetTemporaryProofV1ResponseMPayload(
                a_obj_ezsigndocumentlog = [
                    eZmaxApi.models.ezsigndocumentlog_response_compound.ezsigndocumentlog-ResponseCompound()
                    ]
            )
        else:
            return EzsigndocumentGetTemporaryProofV1ResponseMPayload(
                a_obj_ezsigndocumentlog = [
                    eZmaxApi.models.ezsigndocumentlog_response_compound.ezsigndocumentlog-ResponseCompound()
                    ],
        )
        """

    def testEzsigndocumentGetTemporaryProofV1ResponseMPayload(self):
        """Test EzsigndocumentGetTemporaryProofV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
