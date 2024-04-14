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

from eZmaxApi.models.creditcardclient_list_element import CreditcardclientListElement

class TestCreditcardclientListElement(unittest.TestCase):
    """CreditcardclientListElement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreditcardclientListElement:
        """Test CreditcardclientListElement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreditcardclientListElement`
        """
        model = CreditcardclientListElement()
        if include_optional:
            return CreditcardclientListElement(
                pki_creditcardclient_id = 114,
                fki_creditcarddetail_id = 53,
                b_creditcardclientrelation_isdefault = True,
                s_creditcardclient_description = 'Visa',
                b_creditcardclient_isactive = True,
                b_creditcardclient_allowedagencypayment = True,
                b_creditcardclient_allowedroyallepageprotection = True,
                b_creditcardclient_allowedtranquillit = True,
                i_creditcarddetail_expirationmonth = 10,
                i_creditcarddetail_expirationyear = 2024,
                s_creditcarddetail_numbermasked = 'XXXX XXXX XXXX 4242'
            )
        else:
            return CreditcardclientListElement(
                pki_creditcardclient_id = 114,
                fki_creditcarddetail_id = 53,
                b_creditcardclientrelation_isdefault = True,
                s_creditcardclient_description = 'Visa',
                b_creditcardclient_isactive = True,
                b_creditcardclient_allowedagencypayment = True,
                b_creditcardclient_allowedroyallepageprotection = True,
                b_creditcardclient_allowedtranquillit = True,
                i_creditcarddetail_expirationmonth = 10,
                i_creditcarddetail_expirationyear = 2024,
                s_creditcarddetail_numbermasked = 'XXXX XXXX XXXX 4242',
        )
        """

    def testCreditcardclientListElement(self):
        """Test CreditcardclientListElement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
