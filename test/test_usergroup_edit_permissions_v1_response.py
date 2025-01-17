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

from eZmaxApi.models.usergroup_edit_permissions_v1_response import UsergroupEditPermissionsV1Response

class TestUsergroupEditPermissionsV1Response(unittest.TestCase):
    """UsergroupEditPermissionsV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsergroupEditPermissionsV1Response:
        """Test UsergroupEditPermissionsV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsergroupEditPermissionsV1Response`
        """
        model = UsergroupEditPermissionsV1Response()
        if include_optional:
            return UsergroupEditPermissionsV1Response(
                m_payload = eZmaxApi.models.usergroup_edit_permissions_v1_response_m_payload.usergroup-editPermissions-v1-Response-mPayload(
                    a_pki_permission_id = [
                        31
                        ], )
            )
        else:
            return UsergroupEditPermissionsV1Response(
                m_payload = eZmaxApi.models.usergroup_edit_permissions_v1_response_m_payload.usergroup-editPermissions-v1-Response-mPayload(
                    a_pki_permission_id = [
                        31
                        ], ),
        )
        """

    def testUsergroupEditPermissionsV1Response(self):
        """Test UsergroupEditPermissionsV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
