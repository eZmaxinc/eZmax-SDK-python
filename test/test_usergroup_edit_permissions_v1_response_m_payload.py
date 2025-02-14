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

from eZmaxApi.models.usergroup_edit_permissions_v1_response_m_payload import UsergroupEditPermissionsV1ResponseMPayload

class TestUsergroupEditPermissionsV1ResponseMPayload(unittest.TestCase):
    """UsergroupEditPermissionsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsergroupEditPermissionsV1ResponseMPayload:
        """Test UsergroupEditPermissionsV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsergroupEditPermissionsV1ResponseMPayload`
        """
        model = UsergroupEditPermissionsV1ResponseMPayload()
        if include_optional:
            return UsergroupEditPermissionsV1ResponseMPayload(
                a_pki_permission_id = [
                    31
                    ]
            )
        else:
            return UsergroupEditPermissionsV1ResponseMPayload(
                a_pki_permission_id = [
                    31
                    ],
        )
        """

    def testUsergroupEditPermissionsV1ResponseMPayload(self):
        """Test UsergroupEditPermissionsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
