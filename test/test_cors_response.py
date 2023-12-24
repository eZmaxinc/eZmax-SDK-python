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

from eZmaxApi.models.cors_response import CorsResponse

class TestCorsResponse(unittest.TestCase):
    """CorsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CorsResponse:
        """Test CorsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CorsResponse`
        """
        model = CorsResponse()
        if include_optional:
            return CorsResponse(
                pki_cors_id = 228,
                fki_apikey_id = 99,
                s_cors_entryurl = 'Https://www.example.com'
            )
        else:
            return CorsResponse(
                pki_cors_id = 228,
                fki_apikey_id = 99,
                s_cors_entryurl = 'Https://www.example.com',
        )
        """

    def testCorsResponse(self):
        """Test CorsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
