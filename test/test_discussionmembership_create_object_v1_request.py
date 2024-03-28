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

from eZmaxApi.models.discussionmembership_create_object_v1_request import DiscussionmembershipCreateObjectV1Request

class TestDiscussionmembershipCreateObjectV1Request(unittest.TestCase):
    """DiscussionmembershipCreateObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiscussionmembershipCreateObjectV1Request:
        """Test DiscussionmembershipCreateObjectV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiscussionmembershipCreateObjectV1Request`
        """
        model = DiscussionmembershipCreateObjectV1Request()
        if include_optional:
            return DiscussionmembershipCreateObjectV1Request(
                a_obj_discussionmembership = [
                    eZmaxApi.models.discussionmembership_request_compound.discussionmembership-RequestCompound()
                    ]
            )
        else:
            return DiscussionmembershipCreateObjectV1Request(
                a_obj_discussionmembership = [
                    eZmaxApi.models.discussionmembership_request_compound.discussionmembership-RequestCompound()
                    ],
        )
        """

    def testDiscussionmembershipCreateObjectV1Request(self):
        """Test DiscussionmembershipCreateObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
