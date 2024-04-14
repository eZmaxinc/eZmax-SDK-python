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

from eZmaxApi.models.ezsigndocument_response_compound import EzsigndocumentResponseCompound

class TestEzsigndocumentResponseCompound(unittest.TestCase):
    """EzsigndocumentResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentResponseCompound:
        """Test EzsigndocumentResponseCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentResponseCompound`
        """
        model = EzsigndocumentResponseCompound()
        if include_optional:
            return EzsigndocumentResponseCompound(
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
                i_ezsigndocument_ezsigndiscussiontotal = 14,
                e_ezsigndocument_steptype = 'Sign',
                i_ezsigndocument_stepformtotal = 2,
                i_ezsigndocument_stepformcurrent = 1,
                i_ezsigndocument_stepsignaturetotal = 2,
                i_ezsigndocument_stepsignature_current = 0,
                a_obj_ezsignfoldersignerassociationstatus = [
                    eZmaxApi.models.custom_ezsignfoldersignerassociationstatus_response.Custom-Ezsignfoldersignerassociationstatus-Response(
                        fki_ezsignfoldersignerassociation_id = 20, 
                        s_ezsignfoldersignerassociationstatus_lastname = 'Doe', 
                        s_ezsignfoldersignerassociationstatus_firstname = 'John', 
                        s_ezsignfoldersignerassociationstatus_description_x = 'John Doe', 
                        a_obj_ezsignsignaturestatus = [
                            eZmaxApi.models.custom_ezsignsignaturestatus_response.Custom-Ezsignsignaturestatus-Response(
                                e_ezsignsignaturestatus_steptype = 'Form', 
                                i_ezsignsignaturestatus_step = 1, 
                                i_ezsignsignaturestatus_total = 2, 
                                i_ezsignsignaturestatus_signed = 1, )
                            ], )
                    ]
            )
        else:
            return EzsigndocumentResponseCompound(
                pki_ezsigndocument_id = 97,
                fki_ezsignfolder_id = 33,
                dt_ezsigndocument_duedate = '2020-12-31 23:59:59',
                s_ezsigndocument_name = 'Contract #123',
                e_ezsigndocument_step = 'Completed',
                i_ezsigndocument_order = 1,
                i_ezsigndocument_pagetotal = 4,
                i_ezsigndocument_signaturesigned = 3,
                i_ezsigndocument_signaturetotal = 4,
                i_ezsigndocument_ezsignsignatureattachmenttotal = 3,
                i_ezsigndocument_ezsigndiscussiontotal = 14,
                e_ezsigndocument_steptype = 'Sign',
                i_ezsigndocument_stepformtotal = 2,
                i_ezsigndocument_stepformcurrent = 1,
                i_ezsigndocument_stepsignaturetotal = 2,
                i_ezsigndocument_stepsignature_current = 0,
                a_obj_ezsignfoldersignerassociationstatus = [
                    eZmaxApi.models.custom_ezsignfoldersignerassociationstatus_response.Custom-Ezsignfoldersignerassociationstatus-Response(
                        fki_ezsignfoldersignerassociation_id = 20, 
                        s_ezsignfoldersignerassociationstatus_lastname = 'Doe', 
                        s_ezsignfoldersignerassociationstatus_firstname = 'John', 
                        s_ezsignfoldersignerassociationstatus_description_x = 'John Doe', 
                        a_obj_ezsignsignaturestatus = [
                            eZmaxApi.models.custom_ezsignsignaturestatus_response.Custom-Ezsignsignaturestatus-Response(
                                e_ezsignsignaturestatus_steptype = 'Form', 
                                i_ezsignsignaturestatus_step = 1, 
                                i_ezsignsignaturestatus_total = 2, 
                                i_ezsignsignaturestatus_signed = 1, )
                            ], )
                    ],
        )
        """

    def testEzsigndocumentResponseCompound(self):
        """Test EzsigndocumentResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
