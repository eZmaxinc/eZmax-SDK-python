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

from eZmaxApi.models.creditcarddetail_response_compound import CreditcarddetailResponseCompound

class TestCreditcarddetailResponseCompound(unittest.TestCase):
    """CreditcarddetailResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreditcarddetailResponseCompound:
        """Test CreditcarddetailResponseCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreditcarddetailResponseCompound`
        """
        model = CreditcarddetailResponseCompound()
        if include_optional:
            return CreditcarddetailResponseCompound(
                pki_creditcarddetail_id = 53,
                fki_creditcardtype_id = 2,
                s_creditcarddetail_numbermasked = 'XXXX XXXX XXXX 4242',
                i_creditcarddetail_expirationmonth = 10,
                i_creditcarddetail_expirationyear = 2024,
                s_creditcarddetail_civic = '2500',
                s_creditcarddetail_street = 'Daniel-Johnson Blvd.',
                s_creditcarddetail_zip = 'H7T 2P6'
            )
        else:
            return CreditcarddetailResponseCompound(
                pki_creditcarddetail_id = 53,
                fki_creditcardtype_id = 2,
                s_creditcarddetail_numbermasked = 'XXXX XXXX XXXX 4242',
                i_creditcarddetail_expirationmonth = 10,
                i_creditcarddetail_expirationyear = 2024,
                s_creditcarddetail_civic = '2500',
                s_creditcarddetail_street = 'Daniel-Johnson Blvd.',
                s_creditcarddetail_zip = 'H7T 2P6',
        )
        """

    def testCreditcarddetailResponseCompound(self):
        """Test CreditcarddetailResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()