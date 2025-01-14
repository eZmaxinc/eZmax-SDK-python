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

from eZmaxApi.models.usergroup_edit_usergroupmemberships_v1_request import UsergroupEditUsergroupmembershipsV1Request

class TestUsergroupEditUsergroupmembershipsV1Request(unittest.TestCase):
    """UsergroupEditUsergroupmembershipsV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsergroupEditUsergroupmembershipsV1Request:
        """Test UsergroupEditUsergroupmembershipsV1Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsergroupEditUsergroupmembershipsV1Request`
        """
        model = UsergroupEditUsergroupmembershipsV1Request()
        if include_optional:
            return UsergroupEditUsergroupmembershipsV1Request(
                a_obj_usergroupmembership = [
                    eZmaxApi.models.usergroupmembership_request_compound.usergroupmembership-RequestCompound()
                    ]
            )
        else:
            return UsergroupEditUsergroupmembershipsV1Request(
                a_obj_usergroupmembership = [
                    eZmaxApi.models.usergroupmembership_request_compound.usergroupmembership-RequestCompound()
                    ],
        )
        """

    def testUsergroupEditUsergroupmembershipsV1Request(self):
        """Test UsergroupEditUsergroupmembershipsV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
