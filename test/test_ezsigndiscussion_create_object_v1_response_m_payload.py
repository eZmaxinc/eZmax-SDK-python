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

from eZmaxApi.models.ezsigndiscussion_create_object_v1_response_m_payload import EzsigndiscussionCreateObjectV1ResponseMPayload

class TestEzsigndiscussionCreateObjectV1ResponseMPayload(unittest.TestCase):
    """EzsigndiscussionCreateObjectV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndiscussionCreateObjectV1ResponseMPayload:
        """Test EzsigndiscussionCreateObjectV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndiscussionCreateObjectV1ResponseMPayload`
        """
        model = EzsigndiscussionCreateObjectV1ResponseMPayload()
        if include_optional:
            return EzsigndiscussionCreateObjectV1ResponseMPayload(
                a_pki_ezsigndiscussion_id = [
                    194
                    ]
            )
        else:
            return EzsigndiscussionCreateObjectV1ResponseMPayload(
                a_pki_ezsigndiscussion_id = [
                    194
                    ],
        )
        """

    def testEzsigndiscussionCreateObjectV1ResponseMPayload(self):
        """Test EzsigndiscussionCreateObjectV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
