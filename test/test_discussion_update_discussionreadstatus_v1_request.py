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

from eZmaxApi.models.discussion_update_discussionreadstatus_v1_request import DiscussionUpdateDiscussionreadstatusV1Request

class TestDiscussionUpdateDiscussionreadstatusV1Request(unittest.TestCase):
    """DiscussionUpdateDiscussionreadstatusV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiscussionUpdateDiscussionreadstatusV1Request:
        """Test DiscussionUpdateDiscussionreadstatusV1Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiscussionUpdateDiscussionreadstatusV1Request`
        """
        model = DiscussionUpdateDiscussionreadstatusV1Request()
        if include_optional:
            return DiscussionUpdateDiscussionreadstatusV1Request(
                dt_discussionreadstatus_date = '2020-12-31 23:59:59'
            )
        else:
            return DiscussionUpdateDiscussionreadstatusV1Request(
        )
        """

    def testDiscussionUpdateDiscussionreadstatusV1Request(self):
        """Test DiscussionUpdateDiscussionreadstatusV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
