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

from eZmaxApi.models.cors_create_object_v1_response import CorsCreateObjectV1Response

class TestCorsCreateObjectV1Response(unittest.TestCase):
    """CorsCreateObjectV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CorsCreateObjectV1Response:
        """Test CorsCreateObjectV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CorsCreateObjectV1Response`
        """
        model = CorsCreateObjectV1Response()
        if include_optional:
            return CorsCreateObjectV1Response(
                m_payload = eZmaxApi.models.cors_create_object_v1_response_m_payload.cors-createObject-v1-Response-mPayload(
                    a_pki_cors_id = [
                        228
                        ], )
            )
        else:
            return CorsCreateObjectV1Response(
                m_payload = eZmaxApi.models.cors_create_object_v1_response_m_payload.cors-createObject-v1-Response-mPayload(
                    a_pki_cors_id = [
                        228
                        ], ),
        )
        """

    def testCorsCreateObjectV1Response(self):
        """Test CorsCreateObjectV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
