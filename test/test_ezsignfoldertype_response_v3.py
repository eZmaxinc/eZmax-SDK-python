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

from eZmaxApi.models.ezsignfoldertype_response_v3 import EzsignfoldertypeResponseV3

class TestEzsignfoldertypeResponseV3(unittest.TestCase):
    """EzsignfoldertypeResponseV3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfoldertypeResponseV3:
        """Test EzsignfoldertypeResponseV3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfoldertypeResponseV3`
        """
        model = EzsignfoldertypeResponseV3()
        if include_optional:
            return EzsignfoldertypeResponseV3(
                pki_ezsignfoldertype_id = 5,
                obj_ezsignfoldertype_name = eZmaxApi.models.multilingual_ezsignfoldertype_name.Multilingual-EzsignfoldertypeName(
                    s_ezsignfoldertype_name1 = 'Embauche', 
                    s_ezsignfoldertype_name2 = 'Recruitment', ),
                fki_branding_id = 78,
                fki_billingentityinternal_id = 1,
                fki_ezsigntsarequirement_id = 1,
                s_branding_description_x = 'Company X',
                s_billingentityinternal_description_x = 'Default',
                s_ezsigntsarequirement_description_x = 'No',
                s_email_address_signed = 'email@example.com',
                s_email_address_summary = 'email@example.com',
                e_ezsignfoldertype_privacylevel = 'User',
                e_ezsignfoldertype_sendreminderfrequency = 'None',
                i_ezsignfoldertype_archivaldays = 30,
                e_ezsignfoldertype_disposal = 'Manual',
                e_ezsignfoldertype_completion = 'PerEzsigndocument',
                i_ezsignfoldertype_disposaldays = 365,
                i_ezsignfoldertype_deadlinedays = 5,
                b_ezsignfoldertype_delegate = True,
                b_ezsignfoldertype_discussion = True,
                b_ezsignfoldertype_reassignezsignsigner = True,
                b_ezsignfoldertype_reassignuser = True,
                b_ezsignfoldertype_sendsignedtoezsignsigner = False,
                b_ezsignfoldertype_sendsignedtouser = False,
                b_ezsignfoldertype_sendattachmentezsignsigner = False,
                b_ezsignfoldertype_sendproofezsignsigner = False,
                b_ezsignfoldertype_sendattachmentuser = False,
                b_ezsignfoldertype_sendproofuser = False,
                b_ezsignfoldertype_sendproofemail = False,
                b_ezsignfoldertype_allowdownloadattachmentezsignsigner = False,
                b_ezsignfoldertype_allowdownloadproofezsignsigner = False,
                b_ezsignfoldertype_sendproofreceivealldocument = False,
                b_ezsignfoldertype_sendsignedtodocumentowner = False,
                b_ezsignfoldertype_sendsignedtofolderowner = False,
                b_ezsignfoldertype_sendsignedtofullgroup = False,
                b_ezsignfoldertype_sendsignedtolimitedgroup = False,
                b_ezsignfoldertype_sendsignedtocolleague = False,
                b_ezsignfoldertype_sendsummarytodocumentowner = False,
                b_ezsignfoldertype_sendsummarytofolderowner = False,
                b_ezsignfoldertype_sendsummarytofullgroup = False,
                b_ezsignfoldertype_sendsummarytolimitedgroup = False,
                b_ezsignfoldertype_sendsummarytocolleague = False,
                b_ezsignfoldertype_isactive = True,
                a_obj_userlogintype = [
                    eZmaxApi.models.userlogintype_response.userlogintype-Response(
                        pki_userlogintype_id = 2, 
                        obj_userlogintype_description = eZmaxApi.models.multilingual_userlogintype_description.Multilingual-UserlogintypeDescription(
                            s_userlogintype_description1 = 'Courriel et téléphone ou SMS', 
                            s_userlogintype_description2 = 'Email and phone or SMS', ), 
                        s_userlogintype_description_x = 'Email and phone or SMS', )
                    ],
                a_obj_usergroup_all = [
                    eZmaxApi.models.usergroup_response.usergroup-Response(
                        pki_usergroup_id = 2, 
                        obj_usergroup_name = eZmaxApi.models.multilingual_usergroup_name.Multilingual-UsergroupName(
                            s_usergroup_name1 = 'Direction', 
                            s_usergroup_name2 = 'Management', ), 
                        s_usergroup_name_x = 'Administration', )
                    ],
                a_obj_usergroup_restricted = [
                    eZmaxApi.models.usergroup_response.usergroup-Response(
                        pki_usergroup_id = 2, 
                        obj_usergroup_name = eZmaxApi.models.multilingual_usergroup_name.Multilingual-UsergroupName(
                            s_usergroup_name1 = 'Direction', 
                            s_usergroup_name2 = 'Management', ), 
                        s_usergroup_name_x = 'Administration', )
                    ],
                a_obj_usergroup_template = [
                    eZmaxApi.models.usergroup_response.usergroup-Response(
                        pki_usergroup_id = 2, 
                        obj_usergroup_name = eZmaxApi.models.multilingual_usergroup_name.Multilingual-UsergroupName(
                            s_usergroup_name1 = 'Direction', 
                            s_usergroup_name2 = 'Management', ), 
                        s_usergroup_name_x = 'Administration', )
                    ]
            )
        else:
            return EzsignfoldertypeResponseV3(
                pki_ezsignfoldertype_id = 5,
                obj_ezsignfoldertype_name = eZmaxApi.models.multilingual_ezsignfoldertype_name.Multilingual-EzsignfoldertypeName(
                    s_ezsignfoldertype_name1 = 'Embauche', 
                    s_ezsignfoldertype_name2 = 'Recruitment', ),
                fki_branding_id = 78,
                s_branding_description_x = 'Company X',
                e_ezsignfoldertype_privacylevel = 'User',
                i_ezsignfoldertype_archivaldays = 30,
                e_ezsignfoldertype_disposal = 'Manual',
                e_ezsignfoldertype_completion = 'PerEzsigndocument',
                i_ezsignfoldertype_deadlinedays = 5,
                b_ezsignfoldertype_sendsignedtodocumentowner = False,
                b_ezsignfoldertype_sendsignedtofolderowner = False,
                b_ezsignfoldertype_sendsignedtocolleague = False,
                b_ezsignfoldertype_sendsummarytodocumentowner = False,
                b_ezsignfoldertype_sendsummarytofolderowner = False,
                b_ezsignfoldertype_sendsummarytocolleague = False,
                b_ezsignfoldertype_isactive = True,
                a_obj_userlogintype = [
                    eZmaxApi.models.userlogintype_response.userlogintype-Response(
                        pki_userlogintype_id = 2, 
                        obj_userlogintype_description = eZmaxApi.models.multilingual_userlogintype_description.Multilingual-UserlogintypeDescription(
                            s_userlogintype_description1 = 'Courriel et téléphone ou SMS', 
                            s_userlogintype_description2 = 'Email and phone or SMS', ), 
                        s_userlogintype_description_x = 'Email and phone or SMS', )
                    ],
        )
        """

    def testEzsignfoldertypeResponseV3(self):
        """Test EzsignfoldertypeResponseV3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
