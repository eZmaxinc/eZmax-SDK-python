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

from eZmaxApi.models.attachment_response_compound import AttachmentResponseCompound

class TestAttachmentResponseCompound(unittest.TestCase):
    """AttachmentResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttachmentResponseCompound:
        """Test AttachmentResponseCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttachmentResponseCompound`
        """
        model = AttachmentResponseCompound()
        if include_optional:
            return AttachmentResponseCompound(
                pki_attachment_id = 1,
                fki_computer_id = 249,
                fki_adjustment_id = 202,
                fki_agent_id = 1,
                fki_bankaccount_id = 46,
                fki_broker_id = 26,
                fki_commissionadvance_id = 115,
                fki_communication_id = 1,
                fki_customer_id = 18,
                fki_customertemplate_id = 152,
                fki_deposit_id = 54,
                fki_deposittransitcheque_id = 251,
                fki_electronicfundstransfer_id = 1262,
                fki_employee_id = 31,
                fki_externalbroker_id = 1,
                fki_ezcomadvanceserver_id = 238,
                fki_ezcomcompany_id = 170,
                fki_ezsigndocument_id = 97,
                fki_ghacqcontract_id = 217,
                fki_inscription_id = 17,
                fki_inscriptiontemp_id = 2445,
                fki_inscriptionnotauthenticated_id = 24,
                fki_invoice_id = 1,
                fki_buyercontract_id = 38,
                fki_franchisebroker_id = 61,
                fki_franchiseagence_id = 117,
                fki_franchiseoffice_id = 50,
                fki_franchisefranchise_id = 156,
                fki_franchisecomplaint_id = 24,
                fki_lead_id = 117,
                fki_marketingprogram_id = 178,
                fki_marketingfollow_id = 45,
                fki_notary_id = 1,
                fki_officetaxreport_id = 200,
                fki_otherincome_id = 142,
                fki_paymentpreparation_id = 124,
                fki_purchase_id = 155,
                fki_salary_id = 73,
                fki_supplier_id = 1,
                fki_tranqcontract_id = 39,
                fki_template_id = 232,
                fki_inscriptionchecklist_id = 191,
                fki_folder_id = 81,
                fki_rejectedoffertopurchase_id = 532,
                fki_disclosure_id = 51,
                fki_reconciliation_id = 140,
                fki_ezsigndocument_id_reference = 97,
                e_attachment_documenttype = 'Adjustment',
                s_attachment_name = 'Document.pdf',
                e_attachment_privacy = 'All',
                fki_user_id_specific = 70,
                e_attachment_type = 'Other',
                i_attachment_size = 277465200,
                i_attachment_ed_mmoduleflag = 65,
                s_attachment_md5 = '2cb29026e8a93c930e71598579400db6',
                b_attachment_deleted = False,
                b_attachment_valid = True,
                e_attachment_verified = 'No',
                t_attachment_rejectioncomment = 'Unreadable',
                fki_user_id_owner = 70,
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
                        dt_auditdetail_date = '2020-12-31 23:59:59', ), )
            )
        else:
            return AttachmentResponseCompound(
                pki_attachment_id = 1,
                e_attachment_documenttype = 'Adjustment',
                s_attachment_name = 'Document.pdf',
                e_attachment_privacy = 'All',
                e_attachment_type = 'Other',
                i_attachment_size = 277465200,
                s_attachment_md5 = '2cb29026e8a93c930e71598579400db6',
                b_attachment_deleted = False,
                b_attachment_valid = True,
                e_attachment_verified = 'No',
        )
        """

    def testAttachmentResponseCompound(self):
        """Test AttachmentResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
