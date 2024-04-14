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

from eZmaxApi.models.userstaged_get_object_v2_response_m_payload import UserstagedGetObjectV2ResponseMPayload

class TestUserstagedGetObjectV2ResponseMPayload(unittest.TestCase):
    """UserstagedGetObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserstagedGetObjectV2ResponseMPayload:
        """Test UserstagedGetObjectV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserstagedGetObjectV2ResponseMPayload`
        """
        model = UserstagedGetObjectV2ResponseMPayload()
        if include_optional:
            return UserstagedGetObjectV2ResponseMPayload(
                obj_userstaged = eZmaxApi.models.userstaged_response_compound.userstaged-ResponseCompound()
            )
        else:
            return UserstagedGetObjectV2ResponseMPayload(
                obj_userstaged = eZmaxApi.models.userstaged_response_compound.userstaged-ResponseCompound(),
        )
        """

    def testUserstagedGetObjectV2ResponseMPayload(self):
        """Test UserstagedGetObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
