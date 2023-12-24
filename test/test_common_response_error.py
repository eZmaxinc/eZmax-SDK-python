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

from eZmaxApi.models.common_response_error import CommonResponseError

class TestCommonResponseError(unittest.TestCase):
    """CommonResponseError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonResponseError:
        """Test CommonResponseError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonResponseError`
        """
        model = CommonResponseError()
        if include_optional:
            return CommonResponseError(
                s_error_message = 'Invalid Signature Headers',
                e_error_code = 'BADREQUEST'
            )
        else:
            return CommonResponseError(
                s_error_message = 'Invalid Signature Headers',
                e_error_code = 'BADREQUEST',
        )
        """

    def testCommonResponseError(self):
        """Test CommonResponseError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
