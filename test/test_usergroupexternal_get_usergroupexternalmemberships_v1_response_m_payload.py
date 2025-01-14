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

from eZmaxApi.models.usergroupexternal_get_usergroupexternalmemberships_v1_response_m_payload import UsergroupexternalGetUsergroupexternalmembershipsV1ResponseMPayload

class TestUsergroupexternalGetUsergroupexternalmembershipsV1ResponseMPayload(unittest.TestCase):
    """UsergroupexternalGetUsergroupexternalmembershipsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsergroupexternalGetUsergroupexternalmembershipsV1ResponseMPayload:
        """Test UsergroupexternalGetUsergroupexternalmembershipsV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsergroupexternalGetUsergroupexternalmembershipsV1ResponseMPayload`
        """
        model = UsergroupexternalGetUsergroupexternalmembershipsV1ResponseMPayload()
        if include_optional:
            return UsergroupexternalGetUsergroupexternalmembershipsV1ResponseMPayload(
                a_obj_usergroupexternalmembership = [
                    eZmaxApi.models.usergroupexternalmembership_response_compound.usergroupexternalmembership-ResponseCompound()
                    ]
            )
        else:
            return UsergroupexternalGetUsergroupexternalmembershipsV1ResponseMPayload(
                a_obj_usergroupexternalmembership = [
                    eZmaxApi.models.usergroupexternalmembership_response_compound.usergroupexternalmembership-ResponseCompound()
                    ],
        )
        """

    def testUsergroupexternalGetUsergroupexternalmembershipsV1ResponseMPayload(self):
        """Test UsergroupexternalGetUsergroupexternalmembershipsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
