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

from eZmaxApi.models.creditcardclient_get_object_v2_response_m_payload import CreditcardclientGetObjectV2ResponseMPayload

class TestCreditcardclientGetObjectV2ResponseMPayload(unittest.TestCase):
    """CreditcardclientGetObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreditcardclientGetObjectV2ResponseMPayload:
        """Test CreditcardclientGetObjectV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreditcardclientGetObjectV2ResponseMPayload`
        """
        model = CreditcardclientGetObjectV2ResponseMPayload()
        if include_optional:
            return CreditcardclientGetObjectV2ResponseMPayload(
                obj_creditcardclient = eZmaxApi.models.creditcardclient_response_compound.creditcardclient-ResponseCompound()
            )
        else:
            return CreditcardclientGetObjectV2ResponseMPayload(
                obj_creditcardclient = eZmaxApi.models.creditcardclient_response_compound.creditcardclient-ResponseCompound(),
        )
        """

    def testCreditcardclientGetObjectV2ResponseMPayload(self):
        """Test CreditcardclientGetObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
