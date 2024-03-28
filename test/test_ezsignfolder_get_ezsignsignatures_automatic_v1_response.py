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

from eZmaxApi.models.ezsignfolder_get_ezsignsignatures_automatic_v1_response import EzsignfolderGetEzsignsignaturesAutomaticV1Response

class TestEzsignfolderGetEzsignsignaturesAutomaticV1Response(unittest.TestCase):
    """EzsignfolderGetEzsignsignaturesAutomaticV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfolderGetEzsignsignaturesAutomaticV1Response:
        """Test EzsignfolderGetEzsignsignaturesAutomaticV1Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfolderGetEzsignsignaturesAutomaticV1Response`
        """
        model = EzsignfolderGetEzsignsignaturesAutomaticV1Response()
        if include_optional:
            return EzsignfolderGetEzsignsignaturesAutomaticV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.ezsignfolder_get_ezsignsignatures_automatic_v1_response_m_payload.ezsignfolder-getEzsignsignaturesAutomatic-v1-Response-mPayload(
                    a_e_ezsignsignature_type = [
                        'Name'
                        ], 
                    a_obj_ezsignfolder = [
                        eZmaxApi.models.custom_ezsignfolder_ezsignsignatures_automatic_response.Custom-EzsignfolderEzsignsignaturesAutomatic-Response(
                            pki_ezsignfolder_id = 33, 
                            s_ezsignfolder_description = 'Test eZsign Folder', 
                            a_obj_ezsigndocument = [
                                eZmaxApi.models.custom_ezsigndocument_ezsignsignatures_automatic_response.Custom-EzsigndocumentEzsignsignaturesAutomatic-Response(
                                    pki_ezsigndocument_id = 97, 
                                    s_ezsigndocument_name = 'Contract #123', 
                                    a_obj_ezsignsignature = [
                                        eZmaxApi.models.custom_ezsignsignature_ezsignsignatures_automatic_response.Custom-EzsignsignatureEzsignsignaturesAutomatic-Response(
                                            pki_ezsignsignature_id = 49, 
                                            e_ezsignsignature_type = 'Name', 
                                            i_ezsignpage_pagenumber = 1, )
                                        ], )
                                ], )
                        ], )
            )
        else:
            return EzsignfolderGetEzsignsignaturesAutomaticV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                m_payload = eZmaxApi.models.ezsignfolder_get_ezsignsignatures_automatic_v1_response_m_payload.ezsignfolder-getEzsignsignaturesAutomatic-v1-Response-mPayload(
                    a_e_ezsignsignature_type = [
                        'Name'
                        ], 
                    a_obj_ezsignfolder = [
                        eZmaxApi.models.custom_ezsignfolder_ezsignsignatures_automatic_response.Custom-EzsignfolderEzsignsignaturesAutomatic-Response(
                            pki_ezsignfolder_id = 33, 
                            s_ezsignfolder_description = 'Test eZsign Folder', 
                            a_obj_ezsigndocument = [
                                eZmaxApi.models.custom_ezsigndocument_ezsignsignatures_automatic_response.Custom-EzsigndocumentEzsignsignaturesAutomatic-Response(
                                    pki_ezsigndocument_id = 97, 
                                    s_ezsigndocument_name = 'Contract #123', 
                                    a_obj_ezsignsignature = [
                                        eZmaxApi.models.custom_ezsignsignature_ezsignsignatures_automatic_response.Custom-EzsignsignatureEzsignsignaturesAutomatic-Response(
                                            pki_ezsignsignature_id = 49, 
                                            e_ezsignsignature_type = 'Name', 
                                            i_ezsignpage_pagenumber = 1, )
                                        ], )
                                ], )
                        ], ),
        )
        """

    def testEzsignfolderGetEzsignsignaturesAutomaticV1Response(self):
        """Test EzsignfolderGetEzsignsignaturesAutomaticV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
