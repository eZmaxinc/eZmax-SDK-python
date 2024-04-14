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

from eZmaxApi.models.apikey_get_cors_v1_response_m_payload import ApikeyGetCorsV1ResponseMPayload

class TestApikeyGetCorsV1ResponseMPayload(unittest.TestCase):
    """ApikeyGetCorsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApikeyGetCorsV1ResponseMPayload:
        """Test ApikeyGetCorsV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApikeyGetCorsV1ResponseMPayload`
        """
        model = ApikeyGetCorsV1ResponseMPayload()
        if include_optional:
            return ApikeyGetCorsV1ResponseMPayload(
                a_obj_cors = [
                    eZmaxApi.models.cors_response_compound.cors-ResponseCompound()
                    ]
            )
        else:
            return ApikeyGetCorsV1ResponseMPayload(
                a_obj_cors = [
                    eZmaxApi.models.cors_response_compound.cors-ResponseCompound()
                    ],
        )
        """

    def testApikeyGetCorsV1ResponseMPayload(self):
        """Test ApikeyGetCorsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
