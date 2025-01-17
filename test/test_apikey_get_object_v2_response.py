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

from eZmaxApi.models.apikey_get_object_v2_response import ApikeyGetObjectV2Response

class TestApikeyGetObjectV2Response(unittest.TestCase):
    """ApikeyGetObjectV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApikeyGetObjectV2Response:
        """Test ApikeyGetObjectV2Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApikeyGetObjectV2Response`
        """
        model = ApikeyGetObjectV2Response()
        if include_optional:
            return ApikeyGetObjectV2Response(
                m_payload = eZmaxApi.models.apikey_get_object_v2_response_m_payload.apikey-getObject-v2-Response-mPayload(
                    obj_apikey = eZmaxApi.models.apikey_response_compound.apikey-ResponseCompound(), )
            )
        else:
            return ApikeyGetObjectV2Response(
                m_payload = eZmaxApi.models.apikey_get_object_v2_response_m_payload.apikey-getObject-v2-Response-mPayload(
                    obj_apikey = eZmaxApi.models.apikey_response_compound.apikey-ResponseCompound(), ),
        )
        """

    def testApikeyGetObjectV2Response(self):
        """Test ApikeyGetObjectV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
