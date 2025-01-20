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

from eZmaxApi.models.user_response_compound import UserResponseCompound

class TestUserResponseCompound(unittest.TestCase):
    """UserResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserResponseCompound:
        """Test UserResponseCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserResponseCompound`
        """
        model = UserResponseCompound()
        if include_optional:
            return UserResponseCompound(
                pki_user_id = 70,
                fki_agent_id = 1,
                fki_broker_id = 26,
                fki_assistant_id = 1,
                fki_employee_id = 31,
                fki_company_id_default = 1,
                s_company_name_x = 'Acme inc.',
                fki_department_id_default = 21,
                s_department_name_x = 'Head Office',
                fki_timezone_id = 247,
                s_timezone_name = 'Default',
                fki_language_id = 2,
                s_language_name_x = 'English',
                obj_email = eZmaxApi.models.email_response.email-Response(
                    pki_email_id = 22, 
                    fki_emailtype_id = 1, 
                    s_email_address = 'email@example.com', ),
                fki_billingentityinternal_id = 1,
                s_billingentityinternal_description_x = 'Default',
                obj_phone_home = eZmaxApi.models.phone_response_compound.phone-ResponseCompound(),
                obj_phone_sms = eZmaxApi.models.phone_response_compound.phone-ResponseCompound(),
                fki_secretquestion_id = 7,
                fki_module_id_form = 40,
                s_module_name_x = 'Purchase',
                e_user_origin = 'BuiltIn',
                e_user_type = 'EzsignUser',
                e_user_logintype = 'Password',
                s_user_firstname = 'John',
                s_user_lastname = 'Doe',
                s_user_loginname = 'JohnDoe',
                s_user_jobtitle = 'Sales Representative',
                e_user_ezsignaccess = 'PaidByOffice',
                dt_user_lastlogondate = '2020-12-31 23:59:59',
                dt_user_passwordchanged = '2020-12-31 23:59:59',
                dt_user_ezsignprepaidexpiration = '2020-12-31',
                b_user_isactive = True,
                b_user_validatebyadministration = False,
                b_user_validatebydirector = False,
                b_user_attachmentautoverified = True,
                b_user_changepassword = True,
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
            return UserResponseCompound(
                pki_user_id = 70,
                fki_company_id_default = 1,
                s_company_name_x = 'Acme inc.',
                fki_department_id_default = 21,
                s_department_name_x = 'Head Office',
                fki_timezone_id = 247,
                s_timezone_name = 'Default',
                fki_language_id = 2,
                s_language_name_x = 'English',
                obj_email = eZmaxApi.models.email_response.email-Response(
                    pki_email_id = 22, 
                    fki_emailtype_id = 1, 
                    s_email_address = 'email@example.com', ),
                fki_billingentityinternal_id = 1,
                s_billingentityinternal_description_x = 'Default',
                e_user_origin = 'BuiltIn',
                e_user_type = 'EzsignUser',
                e_user_logintype = 'Password',
                s_user_firstname = 'John',
                s_user_lastname = 'Doe',
                s_user_loginname = 'JohnDoe',
                e_user_ezsignaccess = 'PaidByOffice',
                b_user_isactive = True,
                b_user_changepassword = True,
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

    def testUserResponseCompound(self):
        """Test UserResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
