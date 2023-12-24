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

from eZmaxApi.models.ezsigndocument_get_ezsignannotations_v1_response_m_payload import EzsigndocumentGetEzsignannotationsV1ResponseMPayload

class TestEzsigndocumentGetEzsignannotationsV1ResponseMPayload(unittest.TestCase):
    """EzsigndocumentGetEzsignannotationsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentGetEzsignannotationsV1ResponseMPayload:
        """Test EzsigndocumentGetEzsignannotationsV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentGetEzsignannotationsV1ResponseMPayload`
        """
        model = EzsigndocumentGetEzsignannotationsV1ResponseMPayload()
        if include_optional:
            return EzsigndocumentGetEzsignannotationsV1ResponseMPayload(
                a_obj_ezsignannotation = [
                    eZmaxApi.models.ezsignannotation_response_compound.ezsignannotation-ResponseCompound()
                    ]
            )
        else:
            return EzsigndocumentGetEzsignannotationsV1ResponseMPayload(
                a_obj_ezsignannotation = [
                    eZmaxApi.models.ezsignannotation_response_compound.ezsignannotation-ResponseCompound()
                    ],
        )
        """

    def testEzsigndocumentGetEzsignannotationsV1ResponseMPayload(self):
        """Test EzsigndocumentGetEzsignannotationsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
