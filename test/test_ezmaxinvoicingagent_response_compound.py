"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.16
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.custom_contact_name_response import CustomContactNameResponse
from eZmaxApi.model.ezmaxinvoicingagent_response import EzmaxinvoicingagentResponse
from eZmaxApi.model.ezmaxinvoicingagent_response_compound_all_of import EzmaxinvoicingagentResponseCompoundAllOf
from eZmaxApi.model.field_e_ezmaxinvoicingagent_variationezmax import FieldEEzmaxinvoicingagentVariationezmax
from eZmaxApi.model.field_e_ezmaxinvoicingagent_variationezsign import FieldEEzmaxinvoicingagentVariationezsign
from eZmaxApi.model.field_i_ezmaxinvoicingagent_cloned import FieldIEzmaxinvoicingagentCloned
from eZmaxApi.model.field_i_ezmaxinvoicingagent_commissioncalculation import FieldIEzmaxinvoicingagentCommissioncalculation
from eZmaxApi.model.field_i_ezmaxinvoicingagent_ezsigndocument import FieldIEzmaxinvoicingagentEzsigndocument
from eZmaxApi.model.field_i_ezmaxinvoicingagent_inscription import FieldIEzmaxinvoicingagentInscription
from eZmaxApi.model.field_i_ezmaxinvoicingagent_inscriptionactive import FieldIEzmaxinvoicingagentInscriptionactive
from eZmaxApi.model.field_i_ezmaxinvoicingagent_invoice import FieldIEzmaxinvoicingagentInvoice
from eZmaxApi.model.field_i_ezmaxinvoicingagent_otherincome import FieldIEzmaxinvoicingagentOtherincome
from eZmaxApi.model.field_i_ezmaxinvoicingagent_sale import FieldIEzmaxinvoicingagentSale
from eZmaxApi.model.field_i_ezmaxinvoicingagent_session import FieldIEzmaxinvoicingagentSession
from eZmaxApi.model.field_pki_agent_id import FieldPkiAgentID
from eZmaxApi.model.field_pki_billingentityinternal_id import FieldPkiBillingentityinternalID
from eZmaxApi.model.field_pki_broker_id import FieldPkiBrokerID
from eZmaxApi.model.field_pki_ezmaxinvoicing_id import FieldPkiEzmaxinvoicingID
from eZmaxApi.model.field_pki_ezmaxinvoicingagent_id import FieldPkiEzmaxinvoicingagentID
globals()['CustomContactNameResponse'] = CustomContactNameResponse
globals()['EzmaxinvoicingagentResponse'] = EzmaxinvoicingagentResponse
globals()['EzmaxinvoicingagentResponseCompoundAllOf'] = EzmaxinvoicingagentResponseCompoundAllOf
globals()['FieldEEzmaxinvoicingagentVariationezmax'] = FieldEEzmaxinvoicingagentVariationezmax
globals()['FieldEEzmaxinvoicingagentVariationezsign'] = FieldEEzmaxinvoicingagentVariationezsign
globals()['FieldIEzmaxinvoicingagentCloned'] = FieldIEzmaxinvoicingagentCloned
globals()['FieldIEzmaxinvoicingagentCommissioncalculation'] = FieldIEzmaxinvoicingagentCommissioncalculation
globals()['FieldIEzmaxinvoicingagentEzsigndocument'] = FieldIEzmaxinvoicingagentEzsigndocument
globals()['FieldIEzmaxinvoicingagentInscription'] = FieldIEzmaxinvoicingagentInscription
globals()['FieldIEzmaxinvoicingagentInscriptionactive'] = FieldIEzmaxinvoicingagentInscriptionactive
globals()['FieldIEzmaxinvoicingagentInvoice'] = FieldIEzmaxinvoicingagentInvoice
globals()['FieldIEzmaxinvoicingagentOtherincome'] = FieldIEzmaxinvoicingagentOtherincome
globals()['FieldIEzmaxinvoicingagentSale'] = FieldIEzmaxinvoicingagentSale
globals()['FieldIEzmaxinvoicingagentSession'] = FieldIEzmaxinvoicingagentSession
globals()['FieldPkiAgentID'] = FieldPkiAgentID
globals()['FieldPkiBillingentityinternalID'] = FieldPkiBillingentityinternalID
globals()['FieldPkiBrokerID'] = FieldPkiBrokerID
globals()['FieldPkiEzmaxinvoicingID'] = FieldPkiEzmaxinvoicingID
globals()['FieldPkiEzmaxinvoicingagentID'] = FieldPkiEzmaxinvoicingagentID
from eZmaxApi.model.ezmaxinvoicingagent_response_compound import EzmaxinvoicingagentResponseCompound


class TestEzmaxinvoicingagentResponseCompound(unittest.TestCase):
    """EzmaxinvoicingagentResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzmaxinvoicingagentResponseCompound(self):
        """Test EzmaxinvoicingagentResponseCompound"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzmaxinvoicingagentResponseCompound()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()