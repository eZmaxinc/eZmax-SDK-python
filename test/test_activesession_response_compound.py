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

from eZmaxApi.models.activesession_response_compound import ActivesessionResponseCompound

class TestActivesessionResponseCompound(unittest.TestCase):
    """ActivesessionResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivesessionResponseCompound:
        """Test ActivesessionResponseCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivesessionResponseCompound`
        """
        model = ActivesessionResponseCompound()
        if include_optional:
            return ActivesessionResponseCompound(
                e_activesession_usertype = 'Normal',
                e_activesession_origin = 'BuiltIn',
                e_activesession_weekdaystart = 'Sunday',
                fki_language_id = 2,
                s_company_name_x = 'Acme inc.',
                s_department_name_x = 'Head Office',
                b_activesession_debug = False,
                b_activesession_issuperadmin = False,
                b_activesession_attachment = False,
                b_activesession_canafe = False,
                b_activesession_financial = False,
                b_activesession_realestatecompleted = False,
                e_activesession_ezsign = 'Full',
                e_activesession_ezsignaccess = 'Prepaid',
                e_activesession_ezsignprepaid = 'Basic',
                e_activesession_realestateinprogress = 'Create',
                pks_customer_code = 'demo',
                fki_systemconfigurationtype_id = 28,
                fki_signature_id = 12,
                fki_ezsignuser_id = 94,
                b_systemconfiguration_ezsignpaidbyoffice = True,
                e_systemconfiguration_ezsignofficeplan = 'Standard',
                e_user_ezsignaccess = 'PaidByOffice',
                e_user_ezsignprepaid = 'Basic',
                b_user_ezsigntrial = False,
                dt_user_ezsignprepaidexpiration = '2020-12-31',
                a_pki_permission_id = [
                    53
                    ],
                obj_user_real = eZmaxApi.models.activesession_response_compound_user.activesession-ResponseCompound-User(
                    pki_user_id = 70, 
                    fki_timezone_id = 247, 
                    s_avatar_url = 'http://www.website.com/avatar.jpg', 
                    s_user_firstname = 'John', 
                    s_user_lastname = 'Doe', 
                    s_email_address = 'email@example.com', 
                    e_user_ezsignsendreminderfrequency = 'None', 
                    i_user_interfacecolor = 3752795, 
                    b_user_interfacedark = False, 
                    i_user_listresult = 25, ),
                obj_user_cloned = eZmaxApi.models.activesession_response_compound_user.activesession-ResponseCompound-User(
                    pki_user_id = 70, 
                    fki_timezone_id = 247, 
                    s_avatar_url = 'http://www.website.com/avatar.jpg', 
                    s_user_firstname = 'John', 
                    s_user_lastname = 'Doe', 
                    s_email_address = 'email@example.com', 
                    e_user_ezsignsendreminderfrequency = 'None', 
                    i_user_interfacecolor = 3752795, 
                    b_user_interfacedark = False, 
                    i_user_listresult = 25, ),
                obj_apikey = eZmaxApi.models.activesession_response_compound_apikey.activesession-ResponseCompound-Apikey(
                    pki_apikey_id = 99, 
                    s_apikey_description_x = 'Project X', ),
                a_e_module_internalname = [
                    'Purchases'
                    ]
            )
        else:
            return ActivesessionResponseCompound(
                e_activesession_usertype = 'Normal',
                e_activesession_origin = 'BuiltIn',
                e_activesession_weekdaystart = 'Sunday',
                fki_language_id = 2,
                s_company_name_x = 'Acme inc.',
                s_department_name_x = 'Head Office',
                b_activesession_debug = False,
                b_activesession_issuperadmin = False,
                e_activesession_ezsignaccess = 'Prepaid',
                pks_customer_code = 'demo',
                fki_systemconfigurationtype_id = 28,
                e_user_ezsignaccess = 'PaidByOffice',
                a_pki_permission_id = [
                    53
                    ],
                obj_user_real = eZmaxApi.models.activesession_response_compound_user.activesession-ResponseCompound-User(
                    pki_user_id = 70, 
                    fki_timezone_id = 247, 
                    s_avatar_url = 'http://www.website.com/avatar.jpg', 
                    s_user_firstname = 'John', 
                    s_user_lastname = 'Doe', 
                    s_email_address = 'email@example.com', 
                    e_user_ezsignsendreminderfrequency = 'None', 
                    i_user_interfacecolor = 3752795, 
                    b_user_interfacedark = False, 
                    i_user_listresult = 25, ),
                a_e_module_internalname = [
                    'Purchases'
                    ],
        )
        """

    def testActivesessionResponseCompound(self):
        """Test ActivesessionResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
