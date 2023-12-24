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

from eZmaxApi.models.webhook_ezsign_ezsignsigner_connect import WebhookEzsignEzsignsignerConnect

class TestWebhookEzsignEzsignsignerConnect(unittest.TestCase):
    """WebhookEzsignEzsignsignerConnect unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookEzsignEzsignsignerConnect:
        """Test WebhookEzsignEzsignsignerConnect
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookEzsignEzsignsignerConnect`
        """
        model = WebhookEzsignEzsignsignerConnect()
        if include_optional:
            return WebhookEzsignEzsignsignerConnect(
                obj_webhook = eZmaxApi.models.custom_webhook_response.Custom-Webhook-Response(),
                a_obj_attempt = [
                    eZmaxApi.models.attempt_response_compound.attempt-ResponseCompound()
                    ],
                obj_ezsignfolder = eZmaxApi.models.ezsignfolder_response.ezsignfolder-Response(
                    pki_ezsignfolder_id = 33, 
                    fki_ezsignfoldertype_id = 5, 
                    obj_ezsignfoldertype = eZmaxApi.models.custom_ezsignfoldertype_response.Custom-Ezsignfoldertype-Response(), 
                    s_ezsignfoldertype_name_x = '', 
                    fki_billingentityinternal_id = 1, 
                    s_billingentityinternal_description_x = 'Default', 
                    fki_ezsigntsarequirement_id = 1, 
                    s_ezsigntsarequirement_description_x = 'No', 
                    s_ezsignfolder_description = 'Test eZsign Folder', 
                    t_ezsignfolder_note = 'This is a note', 
                    b_ezsignfolder_isdisposable = False, 
                    e_ezsignfolder_sendreminderfrequency = 'None', 
                    dt_ezsignfolder_delayedsenddate = '2020-12-31T23:59:59.000Z', 
                    dt_ezsignfolder_duedate = '2020-12-31 23:59:59', 
                    dt_ezsignfolder_sentdate = '2020-12-31T23:59:59.000Z', 
                    dt_ezsignfolder_scheduledarchive = '2020-12-31 23:59:59', 
                    dt_ezsignfolder_scheduleddispose = '2020-12-31', 
                    e_ezsignfolder_step = 'Completed', 
                    dt_ezsignfolder_close = '2020-12-31 23:59:59', 
                    t_ezsignfolder_message = 'Hi everyone,

This is the document I need you to review.

Could you sign it before Monday please.

Best Regards.

Mary', 
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
                    s_ezsignfolder_externalid = '{"ID": 1234, "TAGS": ["tag1", "tag2", "tag3"]}', ),
                obj_ezsignfoldersignerassociation = eZmaxApi.models.ezsignfoldersignerassociation_response_compound.ezsignfoldersignerassociation-ResponseCompound()
            )
        else:
            return WebhookEzsignEzsignsignerConnect(
                obj_webhook = eZmaxApi.models.custom_webhook_response.Custom-Webhook-Response(),
                a_obj_attempt = [
                    eZmaxApi.models.attempt_response_compound.attempt-ResponseCompound()
                    ],
                obj_ezsignfoldersignerassociation = eZmaxApi.models.ezsignfoldersignerassociation_response_compound.ezsignfoldersignerassociation-ResponseCompound(),
        )
        """

    def testWebhookEzsignEzsignsignerConnect(self):
        """Test WebhookEzsignEzsignsignerConnect"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
