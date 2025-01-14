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

from eZmaxApi.models.creditcardclient_response import CreditcardclientResponse

class TestCreditcardclientResponse(unittest.TestCase):
    """CreditcardclientResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreditcardclientResponse:
        """Test CreditcardclientResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreditcardclientResponse`
        """
        model = CreditcardclientResponse()
        if include_optional:
            return CreditcardclientResponse(
                pki_creditcardclient_id = 114,
                fki_creditcarddetail_id = 53,
                b_creditcardclientrelation_isdefault = True,
                s_creditcardclient_description = 'Visa',
                b_creditcardclient_allowedcompanypayment = True,
                b_creditcardclient_allowedtranquillit = True,
                obj_creditcarddetail = eZmaxApi.models.creditcarddetail_response_compound.creditcarddetail-ResponseCompound()
            )
        else:
            return CreditcardclientResponse(
                pki_creditcardclient_id = 114,
                fki_creditcarddetail_id = 53,
                b_creditcardclientrelation_isdefault = True,
                s_creditcardclient_description = 'Visa',
                b_creditcardclient_allowedcompanypayment = True,
                b_creditcardclient_allowedtranquillit = True,
                obj_creditcarddetail = eZmaxApi.models.creditcarddetail_response_compound.creditcarddetail-ResponseCompound(),
        )
        """

    def testCreditcardclientResponse(self):
        """Test CreditcardclientResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
