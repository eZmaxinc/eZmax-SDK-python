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

from eZmaxApi.models.ezsignbulksendtransmission_get_forms_data_v1_response_m_payload import EzsignbulksendtransmissionGetFormsDataV1ResponseMPayload

class TestEzsignbulksendtransmissionGetFormsDataV1ResponseMPayload(unittest.TestCase):
    """EzsignbulksendtransmissionGetFormsDataV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignbulksendtransmissionGetFormsDataV1ResponseMPayload:
        """Test EzsignbulksendtransmissionGetFormsDataV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignbulksendtransmissionGetFormsDataV1ResponseMPayload`
        """
        model = EzsignbulksendtransmissionGetFormsDataV1ResponseMPayload()
        if include_optional:
            return EzsignbulksendtransmissionGetFormsDataV1ResponseMPayload(
                a_obj_forms_data_folder = [
                    eZmaxApi.models.custom_forms_data_folder_response.Custom-FormsDataFolder-Response(
                        pki_ezsignfolder_id = 33, 
                        s_ezsignfolder_description = 'Test eZsign Folder', 
                        a_obj_form_data_document = [
                            eZmaxApi.models.custom_form_data_document_response.Custom-FormDataDocument-Response(
                                pki_ezsigndocument_id = 97, 
                                fki_ezsignfolder_id = 33, 
                                s_ezsigndocument_name = 'Contract #123', 
                                dt_modified_date = '2020-12-31 23:59:59', 
                                a_obj_form_data_signer = [
                                    eZmaxApi.models.custom_form_data_signer_response.Custom-FormDataSigner-Response(
                                        fki_ezsignfoldersignerassociation_id = 20, 
                                        fki_user_id = 70, 
                                        s_contact_firstname = 'John', 
                                        s_contact_lastname = 'Doe', 
                                        a_obj_ezsignformfieldgroup = [
                                            eZmaxApi.models.custom_form_data_ezsignformfieldgroup_response.Custom-FormDataEzsignformfieldgroup-Response(
                                                s_ezsignformfieldgroup_label = 'Allergies', 
                                                a_obj_ezsignformfield = [
                                                    eZmaxApi.models.custom_form_data_ezsignformfield_response.Custom-FormDataEzsignformfield-Response(
                                                        s_ezsignformfield_label = 'Peanuts', 
                                                        s_ezsignformfield_value = 'Yes', )
                                                    ], )
                                            ], )
                                    ], )
                            ], )
                    ]
            )
        else:
            return EzsignbulksendtransmissionGetFormsDataV1ResponseMPayload(
                a_obj_forms_data_folder = [
                    eZmaxApi.models.custom_forms_data_folder_response.Custom-FormsDataFolder-Response(
                        pki_ezsignfolder_id = 33, 
                        s_ezsignfolder_description = 'Test eZsign Folder', 
                        a_obj_form_data_document = [
                            eZmaxApi.models.custom_form_data_document_response.Custom-FormDataDocument-Response(
                                pki_ezsigndocument_id = 97, 
                                fki_ezsignfolder_id = 33, 
                                s_ezsigndocument_name = 'Contract #123', 
                                dt_modified_date = '2020-12-31 23:59:59', 
                                a_obj_form_data_signer = [
                                    eZmaxApi.models.custom_form_data_signer_response.Custom-FormDataSigner-Response(
                                        fki_ezsignfoldersignerassociation_id = 20, 
                                        fki_user_id = 70, 
                                        s_contact_firstname = 'John', 
                                        s_contact_lastname = 'Doe', 
                                        a_obj_ezsignformfieldgroup = [
                                            eZmaxApi.models.custom_form_data_ezsignformfieldgroup_response.Custom-FormDataEzsignformfieldgroup-Response(
                                                s_ezsignformfieldgroup_label = 'Allergies', 
                                                a_obj_ezsignformfield = [
                                                    eZmaxApi.models.custom_form_data_ezsignformfield_response.Custom-FormDataEzsignformfield-Response(
                                                        s_ezsignformfield_label = 'Peanuts', 
                                                        s_ezsignformfield_value = 'Yes', )
                                                    ], )
                                            ], )
                                    ], )
                            ], )
                    ],
        )
        """

    def testEzsignbulksendtransmissionGetFormsDataV1ResponseMPayload(self):
        """Test EzsignbulksendtransmissionGetFormsDataV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
