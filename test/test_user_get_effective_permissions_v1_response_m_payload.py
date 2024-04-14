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

from eZmaxApi.models.user_get_effective_permissions_v1_response_m_payload import UserGetEffectivePermissionsV1ResponseMPayload

class TestUserGetEffectivePermissionsV1ResponseMPayload(unittest.TestCase):
    """UserGetEffectivePermissionsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserGetEffectivePermissionsV1ResponseMPayload:
        """Test UserGetEffectivePermissionsV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserGetEffectivePermissionsV1ResponseMPayload`
        """
        model = UserGetEffectivePermissionsV1ResponseMPayload()
        if include_optional:
            return UserGetEffectivePermissionsV1ResponseMPayload(
                a_obj_modulegroup = [
                    eZmaxApi.models.modulegroup_response_compound.modulegroup-ResponseCompound()
                    ]
            )
        else:
            return UserGetEffectivePermissionsV1ResponseMPayload(
                a_obj_modulegroup = [
                    eZmaxApi.models.modulegroup_response_compound.modulegroup-ResponseCompound()
                    ],
        )
        """

    def testUserGetEffectivePermissionsV1ResponseMPayload(self):
        """Test UserGetEffectivePermissionsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
