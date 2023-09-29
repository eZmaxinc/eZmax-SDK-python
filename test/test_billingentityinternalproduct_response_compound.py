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
import datetime

from eZmaxApi.models.billingentityinternalproduct_response_compound import BillingentityinternalproductResponseCompound  # noqa: E501

class TestBillingentityinternalproductResponseCompound(unittest.TestCase):
    """BillingentityinternalproductResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingentityinternalproductResponseCompound:
        """Test BillingentityinternalproductResponseCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingentityinternalproductResponseCompound`
        """
        model = BillingentityinternalproductResponseCompound()  # noqa: E501
        if include_optional:
            return BillingentityinternalproductResponseCompound(
                pki_billingentityinternalproduct_id = 254,
                fki_billingentityinternal_id = 1,
                s_billingentityinternal_description_x = 'Default',
                fki_ezmaxproduct_id = 172,
                s_ezmaxproduct_description_x = 'eZmax (License)',
                fki_billingentityexternal_id = 83,
                s_billingentityexternal_description = 'ACME Inc'
            )
        else:
            return BillingentityinternalproductResponseCompound(
                pki_billingentityinternalproduct_id = 254,
                fki_billingentityinternal_id = 1,
                s_billingentityinternal_description_x = 'Default',
                fki_ezmaxproduct_id = 172,
                s_ezmaxproduct_description_x = 'eZmax (License)',
                fki_billingentityexternal_id = 83,
                s_billingentityexternal_description = 'ACME Inc',
        )
        """

    def testBillingentityinternalproductResponseCompound(self):
        """Test BillingentityinternalproductResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()