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

from eZmaxApi.models.user_edit_colleagues_v2_response_m_payload import UserEditColleaguesV2ResponseMPayload

class TestUserEditColleaguesV2ResponseMPayload(unittest.TestCase):
    """UserEditColleaguesV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserEditColleaguesV2ResponseMPayload:
        """Test UserEditColleaguesV2ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserEditColleaguesV2ResponseMPayload`
        """
        model = UserEditColleaguesV2ResponseMPayload()
        if include_optional:
            return UserEditColleaguesV2ResponseMPayload(
                a_pki_colleague_id = [
                    60
                    ]
            )
        else:
            return UserEditColleaguesV2ResponseMPayload(
                a_pki_colleague_id = [
                    60
                    ],
        )
        """

    def testUserEditColleaguesV2ResponseMPayload(self):
        """Test UserEditColleaguesV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
