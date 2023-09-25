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

from eZmaxApi.models.user_get_object_v2_response_m_payload import UserGetObjectV2ResponseMPayload  # noqa: E501

class TestUserGetObjectV2ResponseMPayload(unittest.TestCase):
    """UserGetObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserGetObjectV2ResponseMPayload:
        """Test UserGetObjectV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserGetObjectV2ResponseMPayload`
        """
        model = UserGetObjectV2ResponseMPayload()  # noqa: E501
        if include_optional:
            return UserGetObjectV2ResponseMPayload(
                obj_user = eZmaxApi.models.user_response_compound.user-ResponseCompound()
            )
        else:
            return UserGetObjectV2ResponseMPayload(
                obj_user = eZmaxApi.models.user_response_compound.user-ResponseCompound(),
        )
        """

    def testUserGetObjectV2ResponseMPayload(self):
        """Test UserGetObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
