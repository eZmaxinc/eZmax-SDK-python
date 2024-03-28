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

from eZmaxApi.models.discussion_request_compound import DiscussionRequestCompound

class TestDiscussionRequestCompound(unittest.TestCase):
    """DiscussionRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiscussionRequestCompound:
        """Test DiscussionRequestCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiscussionRequestCompound`
        """
        model = DiscussionRequestCompound()
        if include_optional:
            return DiscussionRequestCompound(
                pki_discussion_id = 125,
                s_discussion_description = 'John Doe',
                b_discussion_closed = True
            )
        else:
            return DiscussionRequestCompound(
                s_discussion_description = 'John Doe',
        )
        """

    def testDiscussionRequestCompound(self):
        """Test DiscussionRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
