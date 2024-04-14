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

from eZmaxApi.models.user_create_object_v2_response_m_payload import UserCreateObjectV2ResponseMPayload

class TestUserCreateObjectV2ResponseMPayload(unittest.TestCase):
    """UserCreateObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserCreateObjectV2ResponseMPayload:
        """Test UserCreateObjectV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserCreateObjectV2ResponseMPayload`
        """
        model = UserCreateObjectV2ResponseMPayload()
        if include_optional:
            return UserCreateObjectV2ResponseMPayload(
                a_pki_user_id = [
                    70
                    ]
            )
        else:
            return UserCreateObjectV2ResponseMPayload(
                a_pki_user_id = [
                    70
                    ],
        )
        """

    def testUserCreateObjectV2ResponseMPayload(self):
        """Test UserCreateObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
