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

from eZmaxApi.models.usergroupexternal_get_object_v2_response_m_payload import UsergroupexternalGetObjectV2ResponseMPayload

class TestUsergroupexternalGetObjectV2ResponseMPayload(unittest.TestCase):
    """UsergroupexternalGetObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsergroupexternalGetObjectV2ResponseMPayload:
        """Test UsergroupexternalGetObjectV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsergroupexternalGetObjectV2ResponseMPayload`
        """
        model = UsergroupexternalGetObjectV2ResponseMPayload()
        if include_optional:
            return UsergroupexternalGetObjectV2ResponseMPayload(
                obj_usergroupexternal = eZmaxApi.models.usergroupexternal_response_compound.usergroupexternal-ResponseCompound()
            )
        else:
            return UsergroupexternalGetObjectV2ResponseMPayload(
                obj_usergroupexternal = eZmaxApi.models.usergroupexternal_response_compound.usergroupexternal-ResponseCompound(),
        )
        """

    def testUsergroupexternalGetObjectV2ResponseMPayload(self):
        """Test UsergroupexternalGetObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()