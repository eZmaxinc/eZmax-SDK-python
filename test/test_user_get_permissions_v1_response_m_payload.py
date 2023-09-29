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

from eZmaxApi.models.user_get_permissions_v1_response_m_payload import UserGetPermissionsV1ResponseMPayload  # noqa: E501

class TestUserGetPermissionsV1ResponseMPayload(unittest.TestCase):
    """UserGetPermissionsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserGetPermissionsV1ResponseMPayload:
        """Test UserGetPermissionsV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserGetPermissionsV1ResponseMPayload`
        """
        model = UserGetPermissionsV1ResponseMPayload()  # noqa: E501
        if include_optional:
            return UserGetPermissionsV1ResponseMPayload(
                a_obj_modulegroup = [
                    eZmaxApi.models.modulegroup_response_compound.modulegroup-ResponseCompound()
                    ]
            )
        else:
            return UserGetPermissionsV1ResponseMPayload(
                a_obj_modulegroup = [
                    eZmaxApi.models.modulegroup_response_compound.modulegroup-ResponseCompound()
                    ],
        )
        """

    def testUserGetPermissionsV1ResponseMPayload(self):
        """Test UserGetPermissionsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()