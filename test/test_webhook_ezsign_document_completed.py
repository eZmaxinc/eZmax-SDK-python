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

from eZmaxApi.models.webhook_ezsign_document_completed import WebhookEzsignDocumentCompleted

class TestWebhookEzsignDocumentCompleted(unittest.TestCase):
    """WebhookEzsignDocumentCompleted unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookEzsignDocumentCompleted:
        """Test WebhookEzsignDocumentCompleted
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookEzsignDocumentCompleted`
        """
        model = WebhookEzsignDocumentCompleted()
        if include_optional:
            return WebhookEzsignDocumentCompleted(
                obj_webhook = eZmaxApi.models.custom_webhook_response.Custom-Webhook-Response(),
                a_obj_attempt = [
                    eZmaxApi.models.attempt_response_compound.attempt-ResponseCompound()
                    ],
                obj_ezsigndocument = eZmaxApi.models.ezsigndocument_response.ezsigndocument-Response(
                    pki_ezsigndocument_id = 97, 
                    fki_ezsignfolder_id = 33, 
                    fki_ezsignfoldersignerassociation_id_declinedtosign = 20, 
                    dt_ezsigndocument_duedate = '2020-12-31 23:59:59', 
                    dt_ezsignform_completed = '2020-12-31 23:59:59', 
                    fki_language_id = 2, 
                    s_ezsigndocument_name = 'Contract #123', 
                    e_ezsigndocument_step = 'Completed', 
                    dt_ezsigndocument_firstsend = '2020-12-31 23:59:59', 
                    dt_ezsigndocument_lastsend = '2020-12-31 23:59:59', 
                    i_ezsigndocument_order = 1, 
                    i_ezsigndocument_pagetotal = 4, 
                    i_ezsigndocument_signaturesigned = 3, 
                    i_ezsigndocument_signaturetotal = 4, 
                    i_ezsigndocument_formfieldtotal = 4, 
                    s_ezsigndocument_md5initial = '012345678901234567890123456789AB', 
                    t_ezsigndocument_declinedtosignreason = 'The conditions in the contract are different than those discuted', 
                    s_ezsigndocument_md5signed = '012345678901234567890123456789AB', 
                    b_ezsigndocument_ezsignform = True, 
                    b_ezsigndocument_hassignedsignatures = True, 
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
                    s_ezsigndocument_externalid = '{"ID": 1234, "TAGS": ["tag1", "tag2", "tag3"]}', 
                    i_ezsigndocument_ezsignsignatureattachmenttotal = 3, 
                    i_ezsigndocument_ezsigndiscussiontotal = 14, )
            )
        else:
            return WebhookEzsignDocumentCompleted(
                obj_webhook = eZmaxApi.models.custom_webhook_response.Custom-Webhook-Response(),
                a_obj_attempt = [
                    eZmaxApi.models.attempt_response_compound.attempt-ResponseCompound()
                    ],
                obj_ezsigndocument = eZmaxApi.models.ezsigndocument_response.ezsigndocument-Response(
                    pki_ezsigndocument_id = 97, 
                    fki_ezsignfolder_id = 33, 
                    fki_ezsignfoldersignerassociation_id_declinedtosign = 20, 
                    dt_ezsigndocument_duedate = '2020-12-31 23:59:59', 
                    dt_ezsignform_completed = '2020-12-31 23:59:59', 
                    fki_language_id = 2, 
                    s_ezsigndocument_name = 'Contract #123', 
                    e_ezsigndocument_step = 'Completed', 
                    dt_ezsigndocument_firstsend = '2020-12-31 23:59:59', 
                    dt_ezsigndocument_lastsend = '2020-12-31 23:59:59', 
                    i_ezsigndocument_order = 1, 
                    i_ezsigndocument_pagetotal = 4, 
                    i_ezsigndocument_signaturesigned = 3, 
                    i_ezsigndocument_signaturetotal = 4, 
                    i_ezsigndocument_formfieldtotal = 4, 
                    s_ezsigndocument_md5initial = '012345678901234567890123456789AB', 
                    t_ezsigndocument_declinedtosignreason = 'The conditions in the contract are different than those discuted', 
                    s_ezsigndocument_md5signed = '012345678901234567890123456789AB', 
                    b_ezsigndocument_ezsignform = True, 
                    b_ezsigndocument_hassignedsignatures = True, 
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
                    s_ezsigndocument_externalid = '{"ID": 1234, "TAGS": ["tag1", "tag2", "tag3"]}', 
                    i_ezsigndocument_ezsignsignatureattachmenttotal = 3, 
                    i_ezsigndocument_ezsigndiscussiontotal = 14, ),
        )
        """

    def testWebhookEzsignDocumentCompleted(self):
        """Test WebhookEzsignDocumentCompleted"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
