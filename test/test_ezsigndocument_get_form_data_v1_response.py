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

from eZmaxApi.models.ezsigndocument_get_form_data_v1_response import EzsigndocumentGetFormDataV1Response

class TestEzsigndocumentGetFormDataV1Response(unittest.TestCase):
    """EzsigndocumentGetFormDataV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentGetFormDataV1Response:
        """Test EzsigndocumentGetFormDataV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentGetFormDataV1Response`
        """
        model = EzsigndocumentGetFormDataV1Response()
        if include_optional:
            return EzsigndocumentGetFormDataV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, 
                    dt_response_date = '2020-12-31 23:59:59', ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.ezsigndocument_get_form_data_v1_response_m_payload.ezsigndocument-getFormData-v1-Response-mPayload(
                    obj_form_data_document = eZmaxApi.models.custom_form_data_document_response.Custom-FormDataDocument-Response(
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
                            ], ), )
            )
        else:
            return EzsigndocumentGetFormDataV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, 
                    dt_response_date = '2020-12-31 23:59:59', ),
                m_payload = eZmaxApi.models.ezsigndocument_get_form_data_v1_response_m_payload.ezsigndocument-getFormData-v1-Response-mPayload(
                    obj_form_data_document = eZmaxApi.models.custom_form_data_document_response.Custom-FormDataDocument-Response(
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
                            ], ), ),
        )
        """

    def testEzsigndocumentGetFormDataV1Response(self):
        """Test EzsigndocumentGetFormDataV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
