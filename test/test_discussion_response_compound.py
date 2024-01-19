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

from eZmaxApi.models.discussion_response_compound import DiscussionResponseCompound

class TestDiscussionResponseCompound(unittest.TestCase):
    """DiscussionResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiscussionResponseCompound:
        """Test DiscussionResponseCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiscussionResponseCompound`
        """
        model = DiscussionResponseCompound()
        if include_optional:
            return DiscussionResponseCompound(
                pki_discussion_id = 125,
                s_discussion_description = 'John Doe',
                b_discussion_closed = True,
                dt_discussion_lastread = '2020-12-31 23:59:59',
                i_discussionmessage_count = 4,
                i_discussionmessage_countunread = 4,
                obj_discussionconfiguration = eZmaxApi.models.custom_discussionconfiguration_response.Custom-Discussionconfiguration-Response(),
                a_obj_discussionmembership = [
                    eZmaxApi.models.discussionmembership_response_compound.discussionmembership-ResponseCompound()
                    ],
                a_obj_discussionmessage = [
                    eZmaxApi.models.discussionmessage_response_compound.discussionmessage-ResponseCompound()
                    ]
            )
        else:
            return DiscussionResponseCompound(
                pki_discussion_id = 125,
                s_discussion_description = 'John Doe',
                b_discussion_closed = True,
                i_discussionmessage_count = 4,
                i_discussionmessage_countunread = 4,
                a_obj_discussionmembership = [
                    eZmaxApi.models.discussionmembership_response_compound.discussionmembership-ResponseCompound()
                    ],
                a_obj_discussionmessage = [
                    eZmaxApi.models.discussionmessage_response_compound.discussionmessage-ResponseCompound()
                    ],
        )
        """

    def testDiscussionResponseCompound(self):
        """Test DiscussionResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
