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

from eZmaxApi.models.discussionmembership_create_object_v1_response_m_payload import DiscussionmembershipCreateObjectV1ResponseMPayload

class TestDiscussionmembershipCreateObjectV1ResponseMPayload(unittest.TestCase):
    """DiscussionmembershipCreateObjectV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiscussionmembershipCreateObjectV1ResponseMPayload:
        """Test DiscussionmembershipCreateObjectV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiscussionmembershipCreateObjectV1ResponseMPayload`
        """
        model = DiscussionmembershipCreateObjectV1ResponseMPayload()
        if include_optional:
            return DiscussionmembershipCreateObjectV1ResponseMPayload(
                a_pki_discussionmembership_id = [
                    165
                    ]
            )
        else:
            return DiscussionmembershipCreateObjectV1ResponseMPayload(
                a_pki_discussionmembership_id = [
                    165
                    ],
        )
        """

    def testDiscussionmembershipCreateObjectV1ResponseMPayload(self):
        """Test DiscussionmembershipCreateObjectV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
