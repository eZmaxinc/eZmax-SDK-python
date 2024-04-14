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

from eZmaxApi.models.ezmaxinvoicingagent_response_compound import EzmaxinvoicingagentResponseCompound

class TestEzmaxinvoicingagentResponseCompound(unittest.TestCase):
    """EzmaxinvoicingagentResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzmaxinvoicingagentResponseCompound:
        """Test EzmaxinvoicingagentResponseCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzmaxinvoicingagentResponseCompound`
        """
        model = EzmaxinvoicingagentResponseCompound()
        if include_optional:
            return EzmaxinvoicingagentResponseCompound(
                pki_ezmaxinvoicingagent_id = 181,
                fki_ezmaxinvoicing_id = 28,
                fki_billingentityinternal_id = 1,
                s_billingentityinternal_description_x = 'Default',
                fki_agent_id = 1,
                fki_broker_id = 26,
                i_ezmaxinvoicingagent_session = 42,
                i_ezmaxinvoicingagent_cloned = 157,
                i_ezmaxinvoicingagent_invoice = 30,
                i_ezmaxinvoicingagent_inscription = 113,
                i_ezmaxinvoicingagent_inscriptionactive = 51,
                i_ezmaxinvoicingagent_sale = 213,
                i_ezmaxinvoicingagent_otherincome = 198,
                i_ezmaxinvoicingagent_commissioncalculation = 107,
                i_ezmaxinvoicingagent_ezsigndocument = 160,
                b_ezmaxinvoicingagent_ezsignaccount = True,
                b_ezmaxinvoicingagent_billableezmax = True,
                e_ezmaxinvoicingagent_variationezmax = 'Charge',
                b_ezmaxinvoicingagent_billableezsign = True,
                e_ezmaxinvoicingagent_variationezsign = 'Charge',
                obj_contact_name = eZmaxApi.models.custom_contact_name_response.Custom-ContactName-Response(
                    s_contact_firstname = 'John', 
                    s_contact_lastname = 'Doe', 
                    s_contact_company = 'eZmax Solutions Inc.', )
            )
        else:
            return EzmaxinvoicingagentResponseCompound(
                fki_billingentityinternal_id = 1,
                s_billingentityinternal_description_x = 'Default',
                i_ezmaxinvoicingagent_session = 42,
                i_ezmaxinvoicingagent_cloned = 157,
                i_ezmaxinvoicingagent_invoice = 30,
                i_ezmaxinvoicingagent_inscription = 113,
                i_ezmaxinvoicingagent_inscriptionactive = 51,
                i_ezmaxinvoicingagent_sale = 213,
                i_ezmaxinvoicingagent_otherincome = 198,
                i_ezmaxinvoicingagent_commissioncalculation = 107,
                i_ezmaxinvoicingagent_ezsigndocument = 160,
                b_ezmaxinvoicingagent_ezsignaccount = True,
                b_ezmaxinvoicingagent_billableezmax = True,
                e_ezmaxinvoicingagent_variationezmax = 'Charge',
                b_ezmaxinvoicingagent_billableezsign = True,
                e_ezmaxinvoicingagent_variationezsign = 'Charge',
                obj_contact_name = eZmaxApi.models.custom_contact_name_response.Custom-ContactName-Response(
                    s_contact_firstname = 'John', 
                    s_contact_lastname = 'Doe', 
                    s_contact_company = 'eZmax Solutions Inc.', ),
        )
        """

    def testEzmaxinvoicingagentResponseCompound(self):
        """Test EzmaxinvoicingagentResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
