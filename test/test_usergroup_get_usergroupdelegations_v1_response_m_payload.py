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

from eZmaxApi.models.usergroup_get_usergroupdelegations_v1_response_m_payload import UsergroupGetUsergroupdelegationsV1ResponseMPayload

class TestUsergroupGetUsergroupdelegationsV1ResponseMPayload(unittest.TestCase):
    """UsergroupGetUsergroupdelegationsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsergroupGetUsergroupdelegationsV1ResponseMPayload:
        """Test UsergroupGetUsergroupdelegationsV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsergroupGetUsergroupdelegationsV1ResponseMPayload`
        """
        model = UsergroupGetUsergroupdelegationsV1ResponseMPayload()
        if include_optional:
            return UsergroupGetUsergroupdelegationsV1ResponseMPayload(
                a_obj_usergroupdelegation = [
                    eZmaxApi.models.usergroupdelegation_response_compound.usergroupdelegation-ResponseCompound()
                    ]
            )
        else:
            return UsergroupGetUsergroupdelegationsV1ResponseMPayload(
                a_obj_usergroupdelegation = [
                    eZmaxApi.models.usergroupdelegation_response_compound.usergroupdelegation-ResponseCompound()
                    ],
        )
        """

    def testUsergroupGetUsergroupdelegationsV1ResponseMPayload(self):
        """Test UsergroupGetUsergroupdelegationsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
