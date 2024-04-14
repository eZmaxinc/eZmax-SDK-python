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

from eZmaxApi.models.apikey_regenerate_v1_response_m_payload import ApikeyRegenerateV1ResponseMPayload

class TestApikeyRegenerateV1ResponseMPayload(unittest.TestCase):
    """ApikeyRegenerateV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApikeyRegenerateV1ResponseMPayload:
        """Test ApikeyRegenerateV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApikeyRegenerateV1ResponseMPayload`
        """
        model = ApikeyRegenerateV1ResponseMPayload()
        if include_optional:
            return ApikeyRegenerateV1ResponseMPayload(
                obj_apikey = eZmaxApi.models.apikey_response_compound.apikey-ResponseCompound()
            )
        else:
            return ApikeyRegenerateV1ResponseMPayload(
                obj_apikey = eZmaxApi.models.apikey_response_compound.apikey-ResponseCompound(),
        )
        """

    def testApikeyRegenerateV1ResponseMPayload(self):
        """Test ApikeyRegenerateV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
