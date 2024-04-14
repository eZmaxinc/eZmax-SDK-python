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

from eZmaxApi.models.apikey_create_object_v2_request import ApikeyCreateObjectV2Request

class TestApikeyCreateObjectV2Request(unittest.TestCase):
    """ApikeyCreateObjectV2Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApikeyCreateObjectV2Request:
        """Test ApikeyCreateObjectV2Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApikeyCreateObjectV2Request`
        """
        model = ApikeyCreateObjectV2Request()
        if include_optional:
            return ApikeyCreateObjectV2Request(
                a_obj_apikey = [
                    eZmaxApi.models.apikey_request_compound.apikey-RequestCompound()
                    ]
            )
        else:
            return ApikeyCreateObjectV2Request(
                a_obj_apikey = [
                    eZmaxApi.models.apikey_request_compound.apikey-RequestCompound()
                    ],
        )
        """

    def testApikeyCreateObjectV2Request(self):
        """Test ApikeyCreateObjectV2Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
