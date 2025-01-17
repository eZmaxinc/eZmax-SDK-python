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

from eZmaxApi.models.usergroup_get_permissions_v1_response import UsergroupGetPermissionsV1Response

class TestUsergroupGetPermissionsV1Response(unittest.TestCase):
    """UsergroupGetPermissionsV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsergroupGetPermissionsV1Response:
        """Test UsergroupGetPermissionsV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsergroupGetPermissionsV1Response`
        """
        model = UsergroupGetPermissionsV1Response()
        if include_optional:
            return UsergroupGetPermissionsV1Response(
                m_payload = eZmaxApi.models.usergroup_get_permissions_v1_response_m_payload.usergroup-getPermissions-v1-Response-mPayload(
                    a_obj_modulegroup = [
                        eZmaxApi.models.modulegroup_response_compound.modulegroup-ResponseCompound()
                        ], )
            )
        else:
            return UsergroupGetPermissionsV1Response(
                m_payload = eZmaxApi.models.usergroup_get_permissions_v1_response_m_payload.usergroup-getPermissions-v1-Response-mPayload(
                    a_obj_modulegroup = [
                        eZmaxApi.models.modulegroup_response_compound.modulegroup-ResponseCompound()
                        ], ),
        )
        """

    def testUsergroupGetPermissionsV1Response(self):
        """Test UsergroupGetPermissionsV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
