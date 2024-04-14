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

from eZmaxApi.api.object_discussion_api import ObjectDiscussionApi


class TestObjectDiscussionApi(unittest.TestCase):
    """ObjectDiscussionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectDiscussionApi()

    def tearDown(self) -> None:
        pass

    def test_discussion_create_object_v1(self) -> None:
        """Test case for discussion_create_object_v1

        Create a new Discussion
        """
        pass

    def test_discussion_delete_object_v1(self) -> None:
        """Test case for discussion_delete_object_v1

        Delete an existing Discussion
        """
        pass

    def test_discussion_get_object_v2(self) -> None:
        """Test case for discussion_get_object_v2

        Retrieve an existing Discussion
        """
        pass

    def test_discussion_patch_object_v1(self) -> None:
        """Test case for discussion_patch_object_v1

        Patch an existing Discussion
        """
        pass

    def test_discussion_update_discussionreadstatus_v1(self) -> None:
        """Test case for discussion_update_discussionreadstatus_v1

        Update the read status of the discussion
        """
        pass


if __name__ == '__main__':
    unittest.main()