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

from eZmaxApi.models.ezsigntemplatepublic_response_compound import EzsigntemplatepublicResponseCompound

class TestEzsigntemplatepublicResponseCompound(unittest.TestCase):
    """EzsigntemplatepublicResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatepublicResponseCompound:
        """Test EzsigntemplatepublicResponseCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatepublicResponseCompound`
        """
        model = EzsigntemplatepublicResponseCompound()
        if include_optional:
            return EzsigntemplatepublicResponseCompound(
                pki_ezsigntemplatepublic_id = 96,
                fki_ezsignfoldertype_id = 5,
                s_ezsignfoldertype_name_x = 'Default',
                fki_userlogintype_id = 2,
                s_userlogintype_description_x = 'Email and phone or SMS',
                fki_ezsigntemplate_id = 36,
                fki_ezsigntemplatepackage_id = 99,
                s_ezsigntemplatepublic_description = 'Inscription form',
                s_ezsigntemplatepublic_referenceid = '6B29FC40-CA47-1067-B31D-00DD010662DA',
                b_ezsigntemplatepublic_isactive = True,
                t_ezsigntemplatepublic_note = 'This is a note',
                e_ezsigntemplatepublic_limittype = 'Hour',
                i_ezsigntemplatepublic_limit = 10,
                i_ezsigntemplatepublic_limitexceeded = 5,
                dt_ezsigntemplatepublic_limitexceededsince = '2024-05-16 15:12:45',
                s_ezsigntemplatepublic_url = 'https://prod.ezsignsigner.ca-central-1.ezmax.com/ezsigntemplatepublic/{sEzmaxcustomerCode}/{sEzsigntemplatepublicReferenceID}',
                s_ezsigntemplatepublic_ezsigntemplatedescription = 'jUR,rZ#UM/?R,Fp^l6$AR',
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
                a_obj_ezsignfolderezsigntemplatepublic = [
                    eZmaxApi.models.custom_ezsignfolderezsigntemplatepublic_response.Custom-Ezsignfolderezsigntemplatepublic-Response(
                        pki_ezsignfolder_id = 33, 
                        s_ezsignfolder_description = 'Test eZsign Folder', 
                        e_ezsignfolder_step = 'Completed', 
                        i_ezsignfolder_signaturetotal = 4, 
                        i_ezsignfolder_formfieldtotal = 4, 
                        i_ezsignfolder_signaturesigned = 3, 
                        a_obj_ezsignfolderezsigntemplatepublic_signer = [
                            eZmaxApi.models.custom_ezsignfolderezsigntemplatepublic_signer_response.Custom-EzsignfolderezsigntemplatepublicSigner-Response(
                                fki_user_id = 70, 
                                fki_ezsignsignergroup_id = 27, 
                                s_contact_firstname = 'John', 
                                s_contact_lastname = 'Doe', 
                                s_ezsignsignergroup_description_x = 'HR', )
                            ], )
                    ]
            )
        else:
            return EzsigntemplatepublicResponseCompound(
                pki_ezsigntemplatepublic_id = 96,
                fki_ezsignfoldertype_id = 5,
                s_ezsignfoldertype_name_x = 'Default',
                fki_userlogintype_id = 2,
                s_userlogintype_description_x = 'Email and phone or SMS',
                s_ezsigntemplatepublic_description = 'Inscription form',
                s_ezsigntemplatepublic_referenceid = '6B29FC40-CA47-1067-B31D-00DD010662DA',
                b_ezsigntemplatepublic_isactive = True,
                t_ezsigntemplatepublic_note = 'This is a note',
                e_ezsigntemplatepublic_limittype = 'Hour',
                i_ezsigntemplatepublic_limit = 10,
                i_ezsigntemplatepublic_limitexceeded = 5,
                dt_ezsigntemplatepublic_limitexceededsince = '2024-05-16 15:12:45',
                s_ezsigntemplatepublic_url = 'https://prod.ezsignsigner.ca-central-1.ezmax.com/ezsigntemplatepublic/{sEzmaxcustomerCode}/{sEzsigntemplatepublicReferenceID}',
                s_ezsigntemplatepublic_ezsigntemplatedescription = 'jUR,rZ#UM/?R,Fp^l6$AR',
                a_obj_ezsignfolderezsigntemplatepublic = [
                    eZmaxApi.models.custom_ezsignfolderezsigntemplatepublic_response.Custom-Ezsignfolderezsigntemplatepublic-Response(
                        pki_ezsignfolder_id = 33, 
                        s_ezsignfolder_description = 'Test eZsign Folder', 
                        e_ezsignfolder_step = 'Completed', 
                        i_ezsignfolder_signaturetotal = 4, 
                        i_ezsignfolder_formfieldtotal = 4, 
                        i_ezsignfolder_signaturesigned = 3, 
                        a_obj_ezsignfolderezsigntemplatepublic_signer = [
                            eZmaxApi.models.custom_ezsignfolderezsigntemplatepublic_signer_response.Custom-EzsignfolderezsigntemplatepublicSigner-Response(
                                fki_user_id = 70, 
                                fki_ezsignsignergroup_id = 27, 
                                s_contact_firstname = 'John', 
                                s_contact_lastname = 'Doe', 
                                s_ezsignsignergroup_description_x = 'HR', )
                            ], )
                    ],
        )
        """

    def testEzsigntemplatepublicResponseCompound(self):
        """Test EzsigntemplatepublicResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
