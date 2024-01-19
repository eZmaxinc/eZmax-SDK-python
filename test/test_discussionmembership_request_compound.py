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

from eZmaxApi.models.discussionmembership_request_compound import DiscussionmembershipRequestCompound

class TestDiscussionmembershipRequestCompound(unittest.TestCase):
    """DiscussionmembershipRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiscussionmembershipRequestCompound:
        """Test DiscussionmembershipRequestCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiscussionmembershipRequestCompound`
        """
        model = DiscussionmembershipRequestCompound()
        if include_optional:
            return DiscussionmembershipRequestCompound(
                pki_discussionmembership_id = 165,
                fki_discussion_id = 125,
                fki_user_id = 70,
                fki_usergroup_id = 2,
                fki_modulesection_id = 53,
                dt_discussionmembership_joined = '2020-12-31 23:59:59'
            )
        else:
            return DiscussionmembershipRequestCompound(
                fki_discussion_id = 125,
                dt_discussionmembership_joined = '2020-12-31 23:59:59',
        )
        """

    def testDiscussionmembershipRequestCompound(self):
        """Test DiscussionmembershipRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
