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

from eZmaxApi.models.usergroupexternal_get_usergroups_v1_response_m_payload import UsergroupexternalGetUsergroupsV1ResponseMPayload

class TestUsergroupexternalGetUsergroupsV1ResponseMPayload(unittest.TestCase):
    """UsergroupexternalGetUsergroupsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsergroupexternalGetUsergroupsV1ResponseMPayload:
        """Test UsergroupexternalGetUsergroupsV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsergroupexternalGetUsergroupsV1ResponseMPayload`
        """
        model = UsergroupexternalGetUsergroupsV1ResponseMPayload()
        if include_optional:
            return UsergroupexternalGetUsergroupsV1ResponseMPayload(
                a_obj_usergroup = [
                    eZmaxApi.models.usergroup_response_compound.usergroup-ResponseCompound()
                    ]
            )
        else:
            return UsergroupexternalGetUsergroupsV1ResponseMPayload(
                a_obj_usergroup = [
                    eZmaxApi.models.usergroup_response_compound.usergroup-ResponseCompound()
                    ],
        )
        """

    def testUsergroupexternalGetUsergroupsV1ResponseMPayload(self):
        """Test UsergroupexternalGetUsergroupsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()