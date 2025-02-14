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

from eZmaxApi.models.common_response_error_s_temporary_file_url import CommonResponseErrorSTemporaryFileUrl

class TestCommonResponseErrorSTemporaryFileUrl(unittest.TestCase):
    """CommonResponseErrorSTemporaryFileUrl unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonResponseErrorSTemporaryFileUrl:
        """Test CommonResponseErrorSTemporaryFileUrl
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonResponseErrorSTemporaryFileUrl`
        """
        model = CommonResponseErrorSTemporaryFileUrl()
        if include_optional:
            return CommonResponseErrorSTemporaryFileUrl(
                s_error_message = 'Invalid Signature Headers',
                e_error_code = 'BADREQUEST',
                a_s_error_messagedetail = [
                    ''
                    ],
                s_temporary_file_url = 'http://www.example.com/document.pdf'
            )
        else:
            return CommonResponseErrorSTemporaryFileUrl(
                s_error_message = 'Invalid Signature Headers',
                e_error_code = 'BADREQUEST',
        )
        """

    def testCommonResponseErrorSTemporaryFileUrl(self):
        """Test CommonResponseErrorSTemporaryFileUrl"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
