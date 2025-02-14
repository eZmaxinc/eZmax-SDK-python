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

from eZmaxApi.models.creditcardclient_create_object_v1_response_m_payload import CreditcardclientCreateObjectV1ResponseMPayload

class TestCreditcardclientCreateObjectV1ResponseMPayload(unittest.TestCase):
    """CreditcardclientCreateObjectV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreditcardclientCreateObjectV1ResponseMPayload:
        """Test CreditcardclientCreateObjectV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreditcardclientCreateObjectV1ResponseMPayload`
        """
        model = CreditcardclientCreateObjectV1ResponseMPayload()
        if include_optional:
            return CreditcardclientCreateObjectV1ResponseMPayload(
                a_pki_creditcardclient_id = [
                    114
                    ]
            )
        else:
            return CreditcardclientCreateObjectV1ResponseMPayload(
                a_pki_creditcardclient_id = [
                    114
                    ],
        )
        """

    def testCreditcardclientCreateObjectV1ResponseMPayload(self):
        """Test CreditcardclientCreateObjectV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
