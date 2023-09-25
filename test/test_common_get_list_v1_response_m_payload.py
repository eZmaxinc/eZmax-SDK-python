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

from eZmaxApi.models.common_get_list_v1_response_m_payload import CommonGetListV1ResponseMPayload  # noqa: E501

class TestCommonGetListV1ResponseMPayload(unittest.TestCase):
    """CommonGetListV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonGetListV1ResponseMPayload:
        """Test CommonGetListV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonGetListV1ResponseMPayload`
        """
        model = CommonGetListV1ResponseMPayload()  # noqa: E501
        if include_optional:
            return CommonGetListV1ResponseMPayload(
                i_row_returned = 100,
                i_row_filtered = 533
            )
        else:
            return CommonGetListV1ResponseMPayload(
                i_row_returned = 100,
                i_row_filtered = 533,
        )
        """

    def testCommonGetListV1ResponseMPayload(self):
        """Test CommonGetListV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
