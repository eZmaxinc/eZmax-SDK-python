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

from eZmaxApi.models.customer_response import CustomerResponse

class TestCustomerResponse(unittest.TestCase):
    """CustomerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomerResponse:
        """Test CustomerResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomerResponse`
        """
        model = CustomerResponse()
        if include_optional:
            return CustomerResponse(
                pki_customer_id = 18,
                fki_company_id = 1,
                fki_customergroup_id = 229,
                s_customer_name = 'eZmax Solutions',
                fki_contactinformations_id = 55,
                fki_contactcontainer_id = 150,
                fki_image_id = 164,
                fki_glaccountcontainer_id = 66,
                fki_language_id = 2,
                fki_department_id = 21,
                fki_paymentmethod_id = 166,
                fki_electronicfundstransferbankaccount_id = 36,
                fki_electronicfundstransferbankaccount_id_directdebit = 36,
                fki_sendingmethod_id = 223,
                fki_taxassignment_id = 1,
                fki_attendancestatus_id = 170,
                fki_agent_id_variableexpensechargeto = 1,
                fki_broker_id_variableexpensechargeto = 26,
                fki_customer_id_variableexpensechargeto = 18,
                fki_glaccountcontainer_id_variableexpensechargeto = 66,
                fki_agent_id_supplychargechargeto = 1,
                fki_broker_id_supplychargechargeto = 26,
                fki_customer_id_supplychargechargeto = 18,
                fki_glaccountcontainer_id_supplychargechargeto = 66,
                fki_invoicealternatelogo_id = 242,
                fki_synchronizationlinkserver_id = 107,
                efki_user_id = 70,
                efks_customer_code = 'EZMA1',
                s_customer_code = 'EZMA1',
                d_customer_fulltimeequivalent = '4.00',
                i_customer_photocopiercode = 7085237,
                i_customer_longdistancecode = 12316524,
                i_customer_timewindowstart = 172,
                i_customer_timewindowend = 193,
                d_customer_minimumchargeableinterests = '4.00',
                dt_customer_birthdate = '2020-12-31',
                dt_customer_transfer = '2020-12-31 23:59:59',
                dt_customer_transferappointment = '2020-12-31 23:59:59',
                dt_customer_transfersurvey = '2020-12-31 23:59:59',
                b_customer_isactive = True,
                b_customer_variableexpensefinanced = True,
                b_customer_variableexpensefinancedtaxes = True,
                b_customer_supplychargefinanced = True,
                b_customer_supplychargefinancedtaxes = True,
                b_customer_attendance = True,
                e_customer_type = 'Normal',
                e_customer_marketingcorrespondence = 'No',
                b_customer_blackcopycarbon = True,
                b_customer_unsubscribeinfo = True,
                t_customer_comment = 'This is a comment',
                importid = 'jUR,rZ#UM/?'
            )
        else:
            return CustomerResponse(
                pki_customer_id = 18,
                fki_company_id = 1,
                fki_customergroup_id = 229,
                s_customer_name = 'eZmax Solutions',
                fki_contactinformations_id = 55,
                fki_contactcontainer_id = 150,
                fki_image_id = 164,
                fki_glaccountcontainer_id = 66,
                fki_language_id = 2,
                fki_department_id = 21,
                fki_paymentmethod_id = 166,
                fki_electronicfundstransferbankaccount_id = 36,
                fki_electronicfundstransferbankaccount_id_directdebit = 36,
                fki_sendingmethod_id = 223,
                fki_taxassignment_id = 1,
                fki_attendancestatus_id = 170,
                fki_agent_id_variableexpensechargeto = 1,
                fki_broker_id_variableexpensechargeto = 26,
                fki_customer_id_variableexpensechargeto = 18,
                fki_glaccountcontainer_id_variableexpensechargeto = 66,
                fki_agent_id_supplychargechargeto = 1,
                fki_broker_id_supplychargechargeto = 26,
                fki_customer_id_supplychargechargeto = 18,
                fki_glaccountcontainer_id_supplychargechargeto = 66,
                fki_invoicealternatelogo_id = 242,
                fki_synchronizationlinkserver_id = 107,
                s_customer_code = 'EZMA1',
                d_customer_fulltimeequivalent = '4.00',
                i_customer_photocopiercode = 7085237,
                i_customer_longdistancecode = 12316524,
                i_customer_timewindowstart = 172,
                i_customer_timewindowend = 193,
                d_customer_minimumchargeableinterests = '4.00',
                dt_customer_birthdate = '2020-12-31',
                dt_customer_transfer = '2020-12-31 23:59:59',
                dt_customer_transferappointment = '2020-12-31 23:59:59',
                dt_customer_transfersurvey = '2020-12-31 23:59:59',
                b_customer_isactive = True,
                b_customer_variableexpensefinanced = True,
                b_customer_variableexpensefinancedtaxes = True,
                b_customer_supplychargefinanced = True,
                b_customer_supplychargefinancedtaxes = True,
                b_customer_attendance = True,
                e_customer_type = 'Normal',
                e_customer_marketingcorrespondence = 'No',
                b_customer_blackcopycarbon = True,
                b_customer_unsubscribeinfo = True,
                t_customer_comment = 'This is a comment',
        )
        """

    def testCustomerResponse(self):
        """Test CustomerResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
