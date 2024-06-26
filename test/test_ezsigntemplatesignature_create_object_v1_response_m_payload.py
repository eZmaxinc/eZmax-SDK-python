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

from eZmaxApi.models.ezsigntemplatesignature_create_object_v1_response_m_payload import EzsigntemplatesignatureCreateObjectV1ResponseMPayload

class TestEzsigntemplatesignatureCreateObjectV1ResponseMPayload(unittest.TestCase):
    """EzsigntemplatesignatureCreateObjectV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatesignatureCreateObjectV1ResponseMPayload:
        """Test EzsigntemplatesignatureCreateObjectV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatesignatureCreateObjectV1ResponseMPayload`
        """
        model = EzsigntemplatesignatureCreateObjectV1ResponseMPayload()
        if include_optional:
            return EzsigntemplatesignatureCreateObjectV1ResponseMPayload(
                a_pki_ezsigntemplatesignature_id = [
                    99
                    ]
            )
        else:
            return EzsigntemplatesignatureCreateObjectV1ResponseMPayload(
                a_pki_ezsigntemplatesignature_id = [
                    99
                    ],
        )
        """

    def testEzsigntemplatesignatureCreateObjectV1ResponseMPayload(self):
        """Test EzsigntemplatesignatureCreateObjectV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
