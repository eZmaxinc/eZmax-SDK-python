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

from eZmaxApi.models.ezmaxinvoicing_get_provisional_v1_response_m_payload import EzmaxinvoicingGetProvisionalV1ResponseMPayload  # noqa: E501

class TestEzmaxinvoicingGetProvisionalV1ResponseMPayload(unittest.TestCase):
    """EzmaxinvoicingGetProvisionalV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzmaxinvoicingGetProvisionalV1ResponseMPayload:
        """Test EzmaxinvoicingGetProvisionalV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzmaxinvoicingGetProvisionalV1ResponseMPayload`
        """
        model = EzmaxinvoicingGetProvisionalV1ResponseMPayload()  # noqa: E501
        if include_optional:
            return EzmaxinvoicingGetProvisionalV1ResponseMPayload(
                pki_ezmaxinvoicing_id = 28,
                fki_ezmaxinvoicingcontract_id = 28,
                fki_ezmaxpricing_id = 28,
                fki_systemconfigurationtype_id = 28,
                s_systemconfigurationtype_description_x = 'eZsign (Pro)',
                yyyymm_ezmaxinvoicing = '2022-01',
                i_ezmaxinvoicing_days = 28,
                e_ezmaxinvoicing_paymenttype = 'Cheque',
                d_ezmaxinvoicing_rebatepaymenttype = '1.00',
                i_ezmaxinvoicing_contractlength = 1,
                d_ezmaxinvoicing_rebatecontractlength = '1.00',
                b_ezmaxinvoicing_rebate_ezsignallagents = True,
                obj_audit = eZmaxApi.models.common_audit.Common-Audit(
                    obj_auditdetail_created = eZmaxApi.models.common_auditdetail.Common-Auditdetail(
                        fki_user_id = 70, 
                        fki_apikey_id = 99, 
                        s_user_loginname = 'JohnDoe', 
                        s_user_lastname = 'Doe', 
                        s_user_firstname = 'John', 
                        s_apikey_description_x = 'Project X', 
                        dt_auditdetail_date = '2020-12-31 23:59:59', ), 
                    obj_auditdetail_modified = eZmaxApi.models.common_auditdetail.Common-Auditdetail(
                        fki_user_id = 70, 
                        fki_apikey_id = 99, 
                        s_user_loginname = 'JohnDoe', 
                        s_user_lastname = 'Doe', 
                        s_user_firstname = 'John', 
                        s_apikey_description_x = 'Project X', 
                        dt_auditdetail_date = '2020-12-31 23:59:59', ), ),
                obj_ezmaxinvoicingcontract = eZmaxApi.models.ezmaxinvoicingcontract_response_compound.ezmaxinvoicingcontract-ResponseCompound(),
                obj_ezmaxpricing = eZmaxApi.models.custom_ezmaxpricing_response.Custom-Ezmaxpricing-Response(
                    pki_ezmaxpricing_id = 28, 
                    d_ezmaxpricing_rebateezsignallagents = '90.00', 
                    dt_ezmaxpricing_start = '2020-12-31', 
                    dt_ezmaxpricing_end = '2020-12-31', ),
                a_obj_ezmaxinvoicingsummaryglobal = [
                    eZmaxApi.models.ezmaxinvoicingsummaryglobal_response_compound.ezmaxinvoicingsummaryglobal-ResponseCompound()
                    ],
                a_obj_ezmaxinvoicingsummaryexternal = [
                    eZmaxApi.models.ezmaxinvoicingsummaryexternal_response_compound.ezmaxinvoicingsummaryexternal-ResponseCompound()
                    ],
                a_obj_ezmaxinvoicingsummaryinternal = [
                    eZmaxApi.models.ezmaxinvoicingsummaryinternal_response_compound.ezmaxinvoicingsummaryinternal-ResponseCompound()
                    ],
                a_obj_ezmaxinvoicingagent = [
                    eZmaxApi.models.ezmaxinvoicingagent_response_compound.ezmaxinvoicingagent-ResponseCompound()
                    ],
                a_obj_ezmaxinvoicinguser = [
                    eZmaxApi.models.ezmaxinvoicinguser_response_compound.ezmaxinvoicinguser-ResponseCompound()
                    ],
                a_obj_ezmaxinvoicingezsignfolder = [
                    eZmaxApi.models.custom_ezmaxinvoicing_ezsignfolder_response.Custom-EzmaxinvoicingEzsignfolder-Response()
                    ],
                a_obj_ezmaxinvoicingezsigndocument = [
                    eZmaxApi.models.custom_ezmaxinvoicing_ezsigndocument_response.Custom-EzmaxinvoicingEzsigndocument-Response()
                    ]
            )
        else:
            return EzmaxinvoicingGetProvisionalV1ResponseMPayload(
                fki_ezmaxinvoicingcontract_id = 28,
                fki_ezmaxpricing_id = 28,
                fki_systemconfigurationtype_id = 28,
                s_systemconfigurationtype_description_x = 'eZsign (Pro)',
                yyyymm_ezmaxinvoicing = '2022-01',
                i_ezmaxinvoicing_days = 28,
                e_ezmaxinvoicing_paymenttype = 'Cheque',
                d_ezmaxinvoicing_rebatepaymenttype = '1.00',
                i_ezmaxinvoicing_contractlength = 1,
                d_ezmaxinvoicing_rebatecontractlength = '1.00',
                b_ezmaxinvoicing_rebate_ezsignallagents = True,
                obj_ezmaxinvoicingcontract = eZmaxApi.models.ezmaxinvoicingcontract_response_compound.ezmaxinvoicingcontract-ResponseCompound(),
                obj_ezmaxpricing = eZmaxApi.models.custom_ezmaxpricing_response.Custom-Ezmaxpricing-Response(
                    pki_ezmaxpricing_id = 28, 
                    d_ezmaxpricing_rebateezsignallagents = '90.00', 
                    dt_ezmaxpricing_start = '2020-12-31', 
                    dt_ezmaxpricing_end = '2020-12-31', ),
                a_obj_ezmaxinvoicingsummaryglobal = [
                    eZmaxApi.models.ezmaxinvoicingsummaryglobal_response_compound.ezmaxinvoicingsummaryglobal-ResponseCompound()
                    ],
                a_obj_ezmaxinvoicingsummaryexternal = [
                    eZmaxApi.models.ezmaxinvoicingsummaryexternal_response_compound.ezmaxinvoicingsummaryexternal-ResponseCompound()
                    ],
                a_obj_ezmaxinvoicingsummaryinternal = [
                    eZmaxApi.models.ezmaxinvoicingsummaryinternal_response_compound.ezmaxinvoicingsummaryinternal-ResponseCompound()
                    ],
                a_obj_ezmaxinvoicingagent = [
                    eZmaxApi.models.ezmaxinvoicingagent_response_compound.ezmaxinvoicingagent-ResponseCompound()
                    ],
                a_obj_ezmaxinvoicinguser = [
                    eZmaxApi.models.ezmaxinvoicinguser_response_compound.ezmaxinvoicinguser-ResponseCompound()
                    ],
                a_obj_ezmaxinvoicingezsignfolder = [
                    eZmaxApi.models.custom_ezmaxinvoicing_ezsignfolder_response.Custom-EzmaxinvoicingEzsignfolder-Response()
                    ],
                a_obj_ezmaxinvoicingezsigndocument = [
                    eZmaxApi.models.custom_ezmaxinvoicing_ezsigndocument_response.Custom-EzmaxinvoicingEzsigndocument-Response()
                    ],
        )
        """

    def testEzmaxinvoicingGetProvisionalV1ResponseMPayload(self):
        """Test EzmaxinvoicingGetProvisionalV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
