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

from eZmaxApi.models.user_edit_permissions_v1_request import UserEditPermissionsV1Request

class TestUserEditPermissionsV1Request(unittest.TestCase):
    """UserEditPermissionsV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserEditPermissionsV1Request:
        """Test UserEditPermissionsV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserEditPermissionsV1Request`
        """
        model = UserEditPermissionsV1Request()
        if include_optional:
            return UserEditPermissionsV1Request(
                a_obj_permission = [
                    eZmaxApi.models.permission_request_compound.permission-RequestCompound()
                    ]
            )
        else:
            return UserEditPermissionsV1Request(
                a_obj_permission = [
                    eZmaxApi.models.permission_request_compound.permission-RequestCompound()
                    ],
        )
        """

    def testUserEditPermissionsV1Request(self):
        """Test UserEditPermissionsV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
