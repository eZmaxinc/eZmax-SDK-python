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

from eZmaxApi.models.usergroupdelegation_request import UsergroupdelegationRequest

class TestUsergroupdelegationRequest(unittest.TestCase):
    """UsergroupdelegationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsergroupdelegationRequest:
        """Test UsergroupdelegationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsergroupdelegationRequest`
        """
        model = UsergroupdelegationRequest()
        if include_optional:
            return UsergroupdelegationRequest(
                pki_usergroupdelegation_id = 141,
                fki_usergroup_id = 2,
                fki_user_id = 70
            )
        else:
            return UsergroupdelegationRequest(
                fki_usergroup_id = 2,
                fki_user_id = 70,
        )
        """

    def testUsergroupdelegationRequest(self):
        """Test UsergroupdelegationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
