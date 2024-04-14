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

from eZmaxApi.api.object_attachment_api import ObjectAttachmentApi


class TestObjectAttachmentApi(unittest.TestCase):
    """ObjectAttachmentApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectAttachmentApi()

    def tearDown(self) -> None:
        pass

    def test_attachment_download_v1(self) -> None:
        """Test case for attachment_download_v1

        Retrieve the content
        """
        pass

    def test_attachment_get_attachmentlogs_v1(self) -> None:
        """Test case for attachment_get_attachmentlogs_v1

        Retrieve the Attachmentlogs
        """
        pass

    def test_attachment_get_download_url_v1(self) -> None:
        """Test case for attachment_get_download_url_v1

        Retrieve a URL to download attachments.
        """
        pass


if __name__ == '__main__':
    unittest.main()
