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

from eZmaxApi.models.discussionmessage_create_object_v1_response import DiscussionmessageCreateObjectV1Response

class TestDiscussionmessageCreateObjectV1Response(unittest.TestCase):
    """DiscussionmessageCreateObjectV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiscussionmessageCreateObjectV1Response:
        """Test DiscussionmessageCreateObjectV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiscussionmessageCreateObjectV1Response`
        """
        model = DiscussionmessageCreateObjectV1Response()
        if include_optional:
            return DiscussionmessageCreateObjectV1Response(
                m_payload = eZmaxApi.models.discussionmessage_create_object_v1_response_m_payload.discussionmessage-createObject-v1-Response-mPayload(
                    a_pki_discussionmessage_id = [
                        123
                        ], )
            )
        else:
            return DiscussionmessageCreateObjectV1Response(
                m_payload = eZmaxApi.models.discussionmessage_create_object_v1_response_m_payload.discussionmessage-createObject-v1-Response-mPayload(
                    a_pki_discussionmessage_id = [
                        123
                        ], ),
        )
        """

    def testDiscussionmessageCreateObjectV1Response(self):
        """Test DiscussionmessageCreateObjectV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
