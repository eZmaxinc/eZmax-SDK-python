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

from eZmaxApi.models.ezmaxinvoicingsummaryglobal_response_compound import EzmaxinvoicingsummaryglobalResponseCompound

class TestEzmaxinvoicingsummaryglobalResponseCompound(unittest.TestCase):
    """EzmaxinvoicingsummaryglobalResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzmaxinvoicingsummaryglobalResponseCompound:
        """Test EzmaxinvoicingsummaryglobalResponseCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzmaxinvoicingsummaryglobalResponseCompound`
        """
        model = EzmaxinvoicingsummaryglobalResponseCompound()
        if include_optional:
            return EzmaxinvoicingsummaryglobalResponseCompound(
                pki_ezmaxinvoicingsummaryglobal_id = 241,
                fki_ezmaxinvoicing_id = 28,
                fki_ezmaxproduct_id = 172,
                s_ezmaxproduct_description_x = 'eZmax (License)',
                dt_ezmaxinvoicingsummaryglobal_start = '2020-12-31',
                dt_ezmaxinvoicingsummaryglobal_end = '2020-12-31',
                i_ezmaxinvoicingsummaryglobal_days = 30,
                d_ezmaxinvoicingsummaryglobal_countreal = '649.08',
                d_ezmaxinvoicingsummaryglobal_countbilled = '581.56',
                d_ezmaxinvoicingsummaryglobal_subtotal = '200.00',
                d_ezmaxinvoicingsummaryglobal_rebateamount = '0.00',
                d_ezmaxinvoicingsummaryglobal_rebatepercent = '0.00',
                d_ezmaxinvoicingsummaryglobal_rebatetotal = '2.00',
                d_ezmaxinvoicingsummaryglobal_total = '198.00',
                d_ezmaxinvoicingsummaryglobal_representative = '685.88',
                d_ezmaxinvoicingsummaryglobal_partner = '266.49',
                d_ezmaxinvoicingsummaryglobal_net = '521.71',
                b_ezmaxinvoicingsummaryglobal_adjustment = True,
                t_ezmaxproduct_help_x = 'This is an exemple of help message',
                a_obj_ezmaxinvoicingcommission = [
                    eZmaxApi.models.ezmaxinvoicingcommission_response_compound.ezmaxinvoicingcommission-ResponseCompound()
                    ]
            )
        else:
            return EzmaxinvoicingsummaryglobalResponseCompound(
                fki_ezmaxproduct_id = 172,
                s_ezmaxproduct_description_x = 'eZmax (License)',
                dt_ezmaxinvoicingsummaryglobal_start = '2020-12-31',
                dt_ezmaxinvoicingsummaryglobal_end = '2020-12-31',
                i_ezmaxinvoicingsummaryglobal_days = 30,
                d_ezmaxinvoicingsummaryglobal_countreal = '649.08',
                d_ezmaxinvoicingsummaryglobal_countbilled = '581.56',
                d_ezmaxinvoicingsummaryglobal_subtotal = '200.00',
                d_ezmaxinvoicingsummaryglobal_rebateamount = '0.00',
                d_ezmaxinvoicingsummaryglobal_rebatepercent = '0.00',
                d_ezmaxinvoicingsummaryglobal_rebatetotal = '2.00',
                d_ezmaxinvoicingsummaryglobal_total = '198.00',
                b_ezmaxinvoicingsummaryglobal_adjustment = True,
                t_ezmaxproduct_help_x = 'This is an exemple of help message',
        )
        """

    def testEzmaxinvoicingsummaryglobalResponseCompound(self):
        """Test EzmaxinvoicingsummaryglobalResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
