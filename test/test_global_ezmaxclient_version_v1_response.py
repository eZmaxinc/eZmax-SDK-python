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

from eZmaxApi.models.global_ezmaxclient_version_v1_response import GlobalEzmaxclientVersionV1Response  # noqa: E501

class TestGlobalEzmaxclientVersionV1Response(unittest.TestCase):
    """GlobalEzmaxclientVersionV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GlobalEzmaxclientVersionV1Response:
        """Test GlobalEzmaxclientVersionV1Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GlobalEzmaxclientVersionV1Response`
        """
        model = GlobalEzmaxclientVersionV1Response()  # noqa: E501
        if include_optional:
            return GlobalEzmaxclientVersionV1Response(
                s_ezmaxclient_version = ''
            )
        else:
            return GlobalEzmaxclientVersionV1Response(
                s_ezmaxclient_version = '',
        )
        """

    def testGlobalEzmaxclientVersionV1Response(self):
        """Test GlobalEzmaxclientVersionV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
