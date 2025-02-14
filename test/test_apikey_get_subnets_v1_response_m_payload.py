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

from eZmaxApi.models.apikey_get_subnets_v1_response_m_payload import ApikeyGetSubnetsV1ResponseMPayload

class TestApikeyGetSubnetsV1ResponseMPayload(unittest.TestCase):
    """ApikeyGetSubnetsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApikeyGetSubnetsV1ResponseMPayload:
        """Test ApikeyGetSubnetsV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApikeyGetSubnetsV1ResponseMPayload`
        """
        model = ApikeyGetSubnetsV1ResponseMPayload()
        if include_optional:
            return ApikeyGetSubnetsV1ResponseMPayload(
                a_obj_subnet = [
                    eZmaxApi.models.subnet_response_compound.subnet-ResponseCompound()
                    ]
            )
        else:
            return ApikeyGetSubnetsV1ResponseMPayload(
                a_obj_subnet = [
                    eZmaxApi.models.subnet_response_compound.subnet-ResponseCompound()
                    ],
        )
        """

    def testApikeyGetSubnetsV1ResponseMPayload(self):
        """Test ApikeyGetSubnetsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
