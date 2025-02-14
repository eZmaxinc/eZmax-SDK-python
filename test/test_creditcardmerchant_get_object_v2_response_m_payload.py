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

from eZmaxApi.models.creditcardmerchant_get_object_v2_response_m_payload import CreditcardmerchantGetObjectV2ResponseMPayload

class TestCreditcardmerchantGetObjectV2ResponseMPayload(unittest.TestCase):
    """CreditcardmerchantGetObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreditcardmerchantGetObjectV2ResponseMPayload:
        """Test CreditcardmerchantGetObjectV2ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreditcardmerchantGetObjectV2ResponseMPayload`
        """
        model = CreditcardmerchantGetObjectV2ResponseMPayload()
        if include_optional:
            return CreditcardmerchantGetObjectV2ResponseMPayload(
                obj_creditcardmerchant = eZmaxApi.models.creditcardmerchant_response_compound.creditcardmerchant-ResponseCompound()
            )
        else:
            return CreditcardmerchantGetObjectV2ResponseMPayload(
                obj_creditcardmerchant = eZmaxApi.models.creditcardmerchant_response_compound.creditcardmerchant-ResponseCompound(),
        )
        """

    def testCreditcardmerchantGetObjectV2ResponseMPayload(self):
        """Test CreditcardmerchantGetObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
