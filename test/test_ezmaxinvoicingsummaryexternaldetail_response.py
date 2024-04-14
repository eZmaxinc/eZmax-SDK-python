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

from eZmaxApi.models.ezmaxinvoicingsummaryexternaldetail_response import EzmaxinvoicingsummaryexternaldetailResponse

class TestEzmaxinvoicingsummaryexternaldetailResponse(unittest.TestCase):
    """EzmaxinvoicingsummaryexternaldetailResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzmaxinvoicingsummaryexternaldetailResponse:
        """Test EzmaxinvoicingsummaryexternaldetailResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzmaxinvoicingsummaryexternaldetailResponse`
        """
        model = EzmaxinvoicingsummaryexternaldetailResponse()
        if include_optional:
            return EzmaxinvoicingsummaryexternaldetailResponse(
                pki_ezmaxinvoicingsummaryexternaldetail_id = 163,
                fki_ezmaxinvoicingsummaryexternal_id = 177,
                fki_ezmaxproduct_id = 172,
                s_ezmaxproduct_description_x = 'eZmax (License)',
                d_ezmaxinvoicingsummaryexternaldetail_countreal = '815.61',
                d_ezmaxinvoicingsummaryexternaldetail_subtotal = '382.88',
                d_ezmaxinvoicingsummaryexternaldetail_rebate = '608.18',
                d_ezmaxinvoicingsummaryexternaldetail_total = '869.71',
                b_ezmaxinvoicingsummaryexternaldetail_adjustment = True,
                t_ezmaxproduct_help_x = 'This is an exemple of help message'
            )
        else:
            return EzmaxinvoicingsummaryexternaldetailResponse(
                fki_ezmaxproduct_id = 172,
                s_ezmaxproduct_description_x = 'eZmax (License)',
                d_ezmaxinvoicingsummaryexternaldetail_countreal = '815.61',
                d_ezmaxinvoicingsummaryexternaldetail_subtotal = '382.88',
                d_ezmaxinvoicingsummaryexternaldetail_rebate = '608.18',
                d_ezmaxinvoicingsummaryexternaldetail_total = '869.71',
                b_ezmaxinvoicingsummaryexternaldetail_adjustment = True,
                t_ezmaxproduct_help_x = 'This is an exemple of help message',
        )
        """

    def testEzmaxinvoicingsummaryexternaldetailResponse(self):
        """Test EzmaxinvoicingsummaryexternaldetailResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
