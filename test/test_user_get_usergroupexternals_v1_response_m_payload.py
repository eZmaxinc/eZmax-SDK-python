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

from eZmaxApi.models.user_get_usergroupexternals_v1_response_m_payload import UserGetUsergroupexternalsV1ResponseMPayload

class TestUserGetUsergroupexternalsV1ResponseMPayload(unittest.TestCase):
    """UserGetUsergroupexternalsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserGetUsergroupexternalsV1ResponseMPayload:
        """Test UserGetUsergroupexternalsV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserGetUsergroupexternalsV1ResponseMPayload`
        """
        model = UserGetUsergroupexternalsV1ResponseMPayload()
        if include_optional:
            return UserGetUsergroupexternalsV1ResponseMPayload(
                a_obj_usergroupexternal = [
                    eZmaxApi.models.usergroupexternal_response_compound.usergroupexternal-ResponseCompound()
                    ]
            )
        else:
            return UserGetUsergroupexternalsV1ResponseMPayload(
                a_obj_usergroupexternal = [
                    eZmaxApi.models.usergroupexternal_response_compound.usergroupexternal-ResponseCompound()
                    ],
        )
        """

    def testUserGetUsergroupexternalsV1ResponseMPayload(self):
        """Test UserGetUsergroupexternalsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
