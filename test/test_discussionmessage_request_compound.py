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

from eZmaxApi.models.discussionmessage_request_compound import DiscussionmessageRequestCompound

class TestDiscussionmessageRequestCompound(unittest.TestCase):
    """DiscussionmessageRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiscussionmessageRequestCompound:
        """Test DiscussionmessageRequestCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiscussionmessageRequestCompound`
        """
        model = DiscussionmessageRequestCompound()
        if include_optional:
            return DiscussionmessageRequestCompound(
                pki_discussionmessage_id = 123,
                fki_discussion_id = 125,
                fki_discussionmembership_id_actionrequired = 165,
                t_discussionmessage_content = 'Hello, this is an example of content in a message'
            )
        else:
            return DiscussionmessageRequestCompound(
                fki_discussion_id = 125,
                t_discussionmessage_content = 'Hello, this is an example of content in a message',
        )
        """

    def testDiscussionmessageRequestCompound(self):
        """Test DiscussionmessageRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
