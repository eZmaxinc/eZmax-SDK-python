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

from eZmaxApi.models.discussionmessage_create_object_v1_request import DiscussionmessageCreateObjectV1Request

class TestDiscussionmessageCreateObjectV1Request(unittest.TestCase):
    """DiscussionmessageCreateObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiscussionmessageCreateObjectV1Request:
        """Test DiscussionmessageCreateObjectV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiscussionmessageCreateObjectV1Request`
        """
        model = DiscussionmessageCreateObjectV1Request()
        if include_optional:
            return DiscussionmessageCreateObjectV1Request(
                a_obj_discussionmessage = [
                    eZmaxApi.models.discussionmessage_request_compound.discussionmessage-RequestCompound()
                    ]
            )
        else:
            return DiscussionmessageCreateObjectV1Request(
                a_obj_discussionmessage = [
                    eZmaxApi.models.discussionmessage_request_compound.discussionmessage-RequestCompound()
                    ],
        )
        """

    def testDiscussionmessageCreateObjectV1Request(self):
        """Test DiscussionmessageCreateObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
