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

from eZmaxApi.models.usergroup_edit_object_v1_request import UsergroupEditObjectV1Request

class TestUsergroupEditObjectV1Request(unittest.TestCase):
    """UsergroupEditObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsergroupEditObjectV1Request:
        """Test UsergroupEditObjectV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsergroupEditObjectV1Request`
        """
        model = UsergroupEditObjectV1Request()
        if include_optional:
            return UsergroupEditObjectV1Request(
                obj_usergroup = eZmaxApi.models.usergroup_request_compound.usergroup-RequestCompound()
            )
        else:
            return UsergroupEditObjectV1Request(
                obj_usergroup = eZmaxApi.models.usergroup_request_compound.usergroup-RequestCompound(),
        )
        """

    def testUsergroupEditObjectV1Request(self):
        """Test UsergroupEditObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
