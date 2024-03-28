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

from eZmaxApi.models.usergroupexternal_create_object_v1_request import UsergroupexternalCreateObjectV1Request

class TestUsergroupexternalCreateObjectV1Request(unittest.TestCase):
    """UsergroupexternalCreateObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsergroupexternalCreateObjectV1Request:
        """Test UsergroupexternalCreateObjectV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsergroupexternalCreateObjectV1Request`
        """
        model = UsergroupexternalCreateObjectV1Request()
        if include_optional:
            return UsergroupexternalCreateObjectV1Request(
                a_obj_usergroupexternal = [
                    eZmaxApi.models.usergroupexternal_request_compound.usergroupexternal-RequestCompound()
                    ]
            )
        else:
            return UsergroupexternalCreateObjectV1Request(
                a_obj_usergroupexternal = [
                    eZmaxApi.models.usergroupexternal_request_compound.usergroupexternal-RequestCompound()
                    ],
        )
        """

    def testUsergroupexternalCreateObjectV1Request(self):
        """Test UsergroupexternalCreateObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
