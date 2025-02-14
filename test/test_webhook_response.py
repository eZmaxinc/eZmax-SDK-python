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

from eZmaxApi.models.webhook_response import WebhookResponse

class TestWebhookResponse(unittest.TestCase):
    """WebhookResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookResponse:
        """Test WebhookResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookResponse`
        """
        model = WebhookResponse()
        if include_optional:
            return WebhookResponse(
                pki_webhook_id = 77,
                fki_authenticationexternal_id = 56,
                s_webhook_description = 'Import into our system',
                fki_ezsignfoldertype_id = 5,
                s_ezsignfoldertype_name_x = 'Default',
                e_webhook_module = 'Ezsign',
                e_webhook_ezsignevent = 'FolderCompleted',
                e_webhook_managementevent = 'UserCreated',
                s_webhook_url = 'https://www.example.com',
                s_webhook_emailfailed = 'email@example.com',
                s_webhook_apikey = '',
                s_webhook_secret = '',
                b_webhook_isactive = True,
                b_webhook_issigned = True,
                b_webhook_skipsslvalidation = False,
                s_authenticationexternal_description = 'Authentification',
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
            return WebhookResponse(
                pki_webhook_id = 77,
                s_webhook_description = 'Import into our system',
                e_webhook_module = 'Ezsign',
                s_webhook_url = 'https://www.example.com',
                s_webhook_emailfailed = 'email@example.com',
                b_webhook_isactive = True,
                b_webhook_issigned = True,
                b_webhook_skipsslvalidation = False,
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
        )
        """

    def testWebhookResponse(self):
        """Test WebhookResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
